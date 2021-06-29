using System.Collections;
using System.Collections.Generic;
using Fungus;
using UnityEngine;

namespace Fungus {
    [CommandInfo ("Custom",
        "Save Collection",
        "Saves an int, float or string collection into a string variable that is then saved normally with e.g. Save Variable.")]

    [AddComponentMenu ("")]

    public class SaveCollection : Command {

        [VariableProperty (typeof (CollectionVariable))]
        public CollectionVariable collection;
        [Tooltip ("Output string - to be saved normally (with Flowchart/Save Variable command)")]
        [VariableProperty (typeof (StringVariable))]
        public StringVariable serializedString;

        [Tooltip ("Clear the save string before saving (useful when using a dummy string)")]
        public bool clearSaveString = true;
        // These are the symbols that delimit each individual string, by default <> - these can't be used in the body of the string itself! (you can't use [] btw, unless you do some clever regex-canceling magic)
        private char delimiterLeft = '¤';
        private char delimiterRight = '¤';
        // Start is called before the first frame update
        public override void OnEnter () {

            if (clearSaveString) {
                serializedString.Value = "";
            }
            for (int i = 0; i < collection.Value.Count; i++) {
                SerializeString (collection.Value.Get (i).ToString ());
            }
            Debug.Log ("<color=green>Saved collection " + collection.Key + " into " + serializedString.Key + "</color>");
            Continue ();

        }

        void SerializeString (string stringToSerialize) {
            if (stringToSerialize != "") {
                serializedString.Value += delimiterLeft + stringToSerialize + delimiterRight;
            }
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
            return "Saving collection " + collection.Key + " into " + serializedString.Key;
        }
        public override Color GetButtonColor () {
            return new Color32 (45, 198, 234, 255);
        }

    }
}