using System;
using System.Collections;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using Fungus;
using UnityEngine;

namespace Fungus {
    [CommandInfo ("Custom",
        "Load Collection",
        "Loads an int, float or string collection from a string variable created with SaveCollection.")]

    [AddComponentMenu ("")]
    public class LoadCollection : Command {

        [VariableProperty (typeof (CollectionVariable))]
        public CollectionVariable collection;
        [Tooltip ("Input string - created with the SaveCollection command")]
        [VariableProperty (typeof (StringVariable))]
        public StringVariable serializedString;

        [Tooltip ("Clear collection before loading.")]
        public bool clearCollection = true;
        [Tooltip ("Should be left at 0 unless you know what you are doing (e.g. loading several collections from one save string")]
        public IntegerData startIndex;
        // These are the symbols that delimit each individual string, by default <> - these can't be used in the body of the string itself! (you can't use [] btw, unless you do some clever regex-canceling magic)
        private char delimiterLeft = '¤';
        private char delimiterRight = '¤';
        public override void OnEnter () {

            if (clearCollection) { // Clear the collection if asked to - this will also ensure the loaded indices are correct!
                collection.Value.Clear ();
            }

            // Checks for anything between delimiter brackets and then sends the first match onward.
            Regex brackets = new Regex (delimiterLeft + ".*?" + delimiterRight);
            MatchCollection matches = brackets.Matches (serializedString.Value);
            // Sets the size of the Collection to the number of matches
            collection.Value.Resize (matches.Count);

            for (int i = startIndex; i < matches.Count; i++) {
                // trim out the actual text
                string ReqText = matches[i].Value.Trim (new Char[] { delimiterLeft, delimiterRight, ' ' });
                // Parse it to the appropriate value
                if (collection.Value.GetType () == typeof (IntCollection)) {
                    int intVal = -999;
                    int.TryParse (ReqText, out intVal);
                    collection.Value.Set (i, intVal);
                } else if (collection.Value.GetType () == typeof (FloatCollection)) {
                    float floatVal = -999f;
                    float.TryParse (ReqText, out floatVal);
                    collection.Value.Set (i, floatVal);
                } else { // It's a string collection!
                    collection.Value.Set (i, ReqText);
                }
            }
            Debug.Log ("<color=green>Loaded collection " + collection.Key + " from " + serializedString.Key + "</color>");
            Continue ();
        }

        public override string GetSummary () {
            if (collection == null) {
                return "Assign a collection!";
            }
            if (collection.Value == null) {
                return "Collection variable is null!";
            }
            if (collection.Value.GetType () != typeof (IntCollection) &&
                collection.Value.GetType () != typeof (FloatCollection) &&
                collection.Value.GetType () != typeof (StringCollection)) {
                return "Invalid collection type!";
            }
            if (serializedString == null) {
                return "No return variable assigned!";
            }
            return "Loading collection " + collection.Key + " from " + serializedString.Key;
        }
        public override Color GetButtonColor () {
            return new Color32 (45, 198, 234, 255);
        }

    }
}