As a student, I have been tasked with implementing a part of an end-to-end platform that will be used to control the state of electronic devices connected to an ESP32 module. Specifically, I need to write two separate applications: one will serve as an API that can be accessed over the internet, and the other will be used as an Arduino sketch to program the ESP32 module.

To maintain consistency, I have been instructed to use pins 22 and 23 for my Fan and Light pins, respectively. Additionally, I should use the variable names WIFI_USER and WIFI_PASS as the wifi information in my Arduino code.

For the first application, I need to create a function that reads the current temperature from a connected digital temperature sensor. This temperature value will then be used to populate the body of a PUT request that should be sent from the ESP32 to my API.

The second application requires me to include a GET request in the ESP32 module code that should be sent to my API.

To make my API accessible over the internet, I am expected to deploy my server application to an online cloud hosting service like render.com. Before doing this, I need to make sure that my code works from my local machine first and then commit it to GitHub so that render.com has access to it.