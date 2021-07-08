using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using Fungus;

public class OptionManager : MonoBehaviour
{
    
    private static string New_Start = "New_Start";
    private static string Sound_Volume_Pref = "Sound_Volume_Pref";
    private int New_Start_Check;
    public Slider slider;
    public float SoundVolume= 0.5f;
    private static OptionManager instance;

    void Awake(){
        if(instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else if(instance != this)
        {
            Destroy(gameObject);
        }
    }
    public static OptionManager Instance
    {
        get
        {
            if (null == instance)
            {
                return null;
            }
            return instance;
        }
    }
    // Start is called before the first frame update
    void Start()
    {
        New_Start_Check = PlayerPrefs.GetInt(New_Start);

        if(New_Start_Check == 0)
        {
            SoundVolume = .75f;
            slider.value = SoundVolume;

            PlayerPrefs.SetFloat(Sound_Volume_Pref,SoundVolume);
            PlayerPrefs.SetInt(New_Start,-1);
        }
        else{
            SoundVolume = PlayerPrefs.GetFloat(Sound_Volume_Pref);
            slider.value= SoundVolume;
        }
    }
    public void SaveSoundSetting()
    {
        PlayerPrefs.SetFloat(Sound_Volume_Pref,SoundVolume);
    }

    void OnApplicationQuit()
    {
        SaveSoundSetting();
    }

    public void AudioVolumeChange(Slider sli)
    {
        SoundVolume = sli.value;
        PlayerPrefs.SetFloat(Sound_Volume_Pref,SoundVolume);
    }

}