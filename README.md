# Vapi Integration with Twilio

Welcome to the Vapi Twilio sample project! This guide will walk you through integrating Vapi with your Twilio account.

## Getting Started

To set up this project:

1. **Create a Python Virtual Environment**
    
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    
    ```
    
2. **Set Up Environment Variables**
    - Create a `.env` file in your repository:
        
        ```bash
        cp .env.example .env
        
        ```
        
    - Add your `VAPI_PRIVATE_TOKEN` to the `.env` file.
3. **Install Dependencies**
    
    ```bash
    pip install --upgrade pip &&\
		pip install -r requirements.txt
    
    ```
    
4. **Configure Your Twilio Number**
    - Go to your Twilio Console and navigate to your active number.
    - In the Configuration section, change the "A call comes in" setting to Webhook.
    - Set the webhook URL to `your_ngrok_url/twilio/inbound_call` and save the configuration.
5. **Run the FastAPI Server**
    
    ```bash
    fastapi dev ./app/main.py   
    
    ```
    

### Exposing Localhost to the Internet

To make your local server accessible over the internet, you can use ngrok. Follow these steps:

1. **Install ngrok**
    - Download ngrok from the official website.
    - Unzip and install ngrok.
2. **Expose Localhost**
    
    ```bash
    ngrok http 8000
    
    ```
    
### Obtaining Assistant ID and Phone Number ID

1. **Assistant ID**: After creating an assistant in the VAPI Dashboard, you will receive an assistant ID. Use this ID in your configurations.
2. **Phone Number ID**: Purchase a Twilio phone number. The ID of this phone number can be used for your purposes.

## Conclusion

This sample project demonstrates how to integrate a custom language model with Vapi. By following these steps, developers can create a more versatile and responsive voice assistant tailored to their users' unique needs.

For more help and detailed documentation, please refer to the official [Vapi documentation](https://docs.vapi.ai/).
