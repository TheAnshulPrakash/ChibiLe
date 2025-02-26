# ChibiLe
This project focuses on controlling smart home based iot devices over serial communication

It is also equipped with a simple anime inspired GUI to display its functionality

##### Referenced libraries 
-WhisperAI by OpenAi ("Small") for speech to text model

-serial to Communicate devices over Serial Ports

### Class Description:

###### Data_sharing: 
**whisper_data** (maxsize=1)

**comm_port** (maxsize=1)

###### WhisperAI: 
Captures real time audio for 5 seconds from mic and converts it to text

*The converted text is stored in the queue **whisper_data***

*runs as a separate thread **t1** in order to only consume memory when required* 

###### Theme:
DropDownMenu

- theme_select : Lets the user choose between 2 predefined theme (light and dark) and also 


    
