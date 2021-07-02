using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using Fungus;

public class UI_Manager : MonoBehaviour
{
    public static UI_Manager instance;
    
    void Awake(){
        if(instance == null)
        {
            instance = this;
        }
        else if(instance != this)
        {
            Destroy(gameObject);
        }
        DontDestroyOnLoad(gameObject);
    }
    public void Start_Btn_Click()
    {
        try{
            var Savemenu = GameObject.Find("SaveMenu");
            Savemenu.transform.Find("Buttons").Find("MenuButton").gameObject.SetActive(true);
            SaveMenu a = Savemenu.gameObject.GetComponent<SaveMenu>();
            a.hasLoadedOnStart = true;

            NarrativeLogMenu b = Savemenu.gameObject.GetComponent<NarrativeLogMenu>();
            b.OnSaveReset();
        }
        catch (NullReferenceException){
            Debug.Log("아직 버튼이 생성되지 않았습니다");
        }
        finally{
            SceneLoader.instance.load("InGame_1");
        }
    }
    public void Load_Btn_Click()
    {
        try{
            var Savemenu = GameObject.Find("SaveMenu");
            Savemenu.transform.Find("Buttons").Find("MenuButton").gameObject.SetActive(true);
            SaveMenu a = Savemenu.gameObject.GetComponent<SaveMenu>();
            a.hasLoadedOnStart = false;
        }
        catch (NullReferenceException){
            Debug.Log("아직 버튼이 생성되지 않았습니다");
        }
        finally{
            SceneLoader.instance.load("InGame_1");
        }
    }
    public void Quit_Btn_Click()
    {
        Application.Quit();
    }
}
