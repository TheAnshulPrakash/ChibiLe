# ChibiLe
This project focuses on controlling smart home based iot devices over serial communication

It is also equipped with a simple anime inspired GUI to display its functionality

##### Referenced libraries 
-WhisperAI by OpenAi for speech to text model

-serial to Communicate devices over Serial Ports

### Class Description:

###### Data_sharing: 
**whisper_data** (maxsize=1)

**comm_port** 

###### WhisperAI: 
Captures real time audio for 5 seconds from mic and converts it to text

*The converted text is stored in the queue **whisper_data***

*runs as a separate thread **t1** in order to only consume memory when required* 

###### Theme:
DropDownMenu

- theme_select : Lets the user choose between 2 predefined theme (light and dark) and also this function is responisble for the drop down of Theme Dropdown
- on_selection_change : This function is called by theme_select whenever the user chooses a different option from the Theme Dropdown also converting the various frames and windows to the desired colour
- port_select : Responsible to select the desired port to establish serial communication with and also places the port dropdown to the desired frame 

###### SerialComm:
SerialCommunication

*Runs as a different Thread **t3***

- connect : To try to connect to the selected port -- *updates comm_port value to "Connected" if the connection is established else throws an error*
- read_Serial : Reads the data of the Serial Device at a specific baud rate
- send_message : Takes string as parameter and sends it to the serial device
- disconnect : Frees the port to be used by other resources

###### Icon:
HomuChan_icon : Responsible for the app tile icon and the default image upon opening

###### Buttons:
ButtonFrame

- clickable_buttons : Contains 5 clickable buttons which can be used for any defined purpose
- slider : Contains a slider which can be used for any Display or Set value

###### Display:
DialogBox:

- output_box : Creates a widget TextBox to diplay whatever WhisperAI  is transcribing
- text_whisper : Continuously updates the output_box based on the text recieved from whisper_data (*Runs as a different Thread **t2***)
- Serial_Box : Creates a widget TextBox to display the output over Serial Communication 
- text_serial : Continuosly updates the Serial_Box based on the text recieved by serial port
- Serial_enter : Creates a separate widget TextBox to get the user input to send it to device
- clear_text : To clear all the texts of the output_box
- clear_text_1 : To clear all the texts of the Serial_Box
- get_text : Maybe used to fetch texts of output_box

###### TrySelf:

***The main class to call different files and their classes and pass their respective frames on where to place them***

Contains different frames to place different widgets

This project is made keeping in mind to be completely customizable by the end user by some minor tweaks

### Basic Info:

***This project uses Whisper AI model ("small") which on real time StT model consumes Memory of around***

***Default Baud Rate for communication is 115200 which can be changed under function 'port_select' in the class DropDownMenu***

### Currently Working On:

* To be able to communicate to devices over WiFi communications
* To perform Robot functions on computer
* To also use LLM TtT models to understand basic speech and perform operations
* To add more custom themes

