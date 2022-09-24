using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using Fungus;

public class OptionManager : MonoBehaviour
{
    
    private static string New_Start = "New_Start";
    private static string Sound_Volume_Pref = "Sound_Volume_Pref";
    private static string Sound_Volume_Pref_Now = "Sound_Volume_Pref_Now";
    private int New_Start_Check;
    public Slider slider;
    public float SoundVolume= 0.5f;
    public GameObject Sound_On;
    public GameObject Sound_Off;
    bool SoundMute;
   
    // Start is called before the first frame update
    void Start()
    {
        New_Start_Check = PlayerPrefs.GetInt(New_Start);
        SoundMute = false;

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

    public void ToggleSoundMute()
    {
        SoundMute = !SoundMute;
        if(SoundMute == true)
        {
            Sound_On.SetActive(!SoundMute);
            Sound_Off.SetActive(SoundMute);

            PlayerPrefs.SetFloat(Sound_Volume_Pref_Now,SoundVolume);

            slider.value = 0f;
            AudioVolumeChange(slider);
        }
        else
        {
            Sound_On.SetActive(!SoundMute);
            Sound_Off.SetActive(SoundMute);

            slider.value = PlayerPrefs.GetFloat(Sound_Volume_Pref_Now);
            AudioVolumeChange(slider);
        }
    }

}