using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using Fungus;

public class UI_Manager : MonoBehaviour
{
    public static UI_Manager instance;

    public GameObject New_Start_Warning_Panel;
    public GameObject Option_UI_Panel;
    
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
    void Start()
    {
        New_Start_Warning_Panel.SetActive(false);
        Option_UI_Panel.SetActive(false);
    }
    public void New_Start_Btn_Click()
    {
        try{
            var Main_UI = GameObject.Find("Main_UI");
            Main_UI.transform.Find("New_Start_Panel").gameObject.SetActive(false);

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

    public void New_Start_Warning()
    {
        var Main_UI = GameObject.Find("Main_UI");
        Main_UI.transform.Find("New_Start_Panel").gameObject.SetActive(true);

        Main_UI.transform.Find("Option_Window").gameObject.SetActive(false);
    }
    public void New_Start_Cancel()
    {
        var Main_UI = GameObject.Find("Main_UI");
        Main_UI.transform.Find("New_Start_Panel").gameObject.SetActive(false);
    }
    public void Option_Btn_Click()
    {
        var Main_UI = GameObject.Find("Main_UI");
        Main_UI.transform.Find("New_Start_Panel").gameObject.SetActive(false);

        Main_UI.transform.Find("Option_Window").gameObject.SetActive(true);
    }
    public void Close_Btn_Click()
    {
        var Main_UI = GameObject.Find("Main_UI");
        Main_UI.transform.Find("Option_Window").gameObject.SetActive(false);
    }
}
