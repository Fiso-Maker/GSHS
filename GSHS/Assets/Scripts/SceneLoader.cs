using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System;
public class SceneLoader : MonoBehaviour
{
    public static SceneLoader instance;

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
    public void load(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
    }

    public void Start_Btn_Click()
    {
        try{
            var SaveMenu = GameObject.Find("SaveMenu");
            SaveMenu.transform.Find("Buttons").Find("MenuButton").gameObject.SetActive(true);
        }
        catch (NullReferenceException){
            Debug.Log("아직 버튼이 생성되지 않았습니다");
        }
        finally{
            load("InGame_1");
        }
    }
    public void Load_Btn_Click()
    {

    }
}