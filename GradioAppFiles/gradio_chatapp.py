import gradio as gr
from vllm import LLM, SamplingParams

# Loading models with sampling params gotten from Deepseek's page
llm = LLM(model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
sampling_params = SamplingParams(temperature=0.6, max_tokens=4096)

# Function runs VLLM and gets a response, history for saving conversations,
def predict(message, history, keep_thinking):
    #Appending the OpenAI style tuples for chat conversation (both VLLM and Gradio require it)
    history.append({"role": "user", "content": message})
    #Generate a response using the chat template from VLLM
    generator = llm.chat(history, sampling_params=sampling_params)
    
    #looping through the generated response to get the string the LLM generated
    for output in generator:
        generated=output.outputs[0].text
    #Split the <think> process for displaying output with or without it
    outputs = generated.split("</think>")[-1]
    think = f"**THINKING PROCESS**\n\n{generated.split("</think")[0]}\n**END OF THINKING**"
    #Checking to see if the Gradio checkbox for keeping <think> is on or off
    if keep_thinking:
        history.append({"role": "assistant", "content": f"{think}{outputs}"})
    else:
        history.append({"role": "assistant", "content": outputs})     
        
    return "",history
    

with gr.Blocks() as demo:
    #Markdown, basically a fancy title ontop
    gr.Markdown("Simple Chatbot")
    #the chatbot method for gradio, it requires OpenAI style tuples
    chat_bot=gr.Chatbot(type= "messages")
    msg= gr.Textbox()
    # keep_thinking is a checkbox to keep the <think></think> process in history and responses
    keep_thinking = gr.Checkbox(label="Keep thinking process in history", value=True)
    #Update/Submit response and execute the predict function, the variables in the list are function parameters
    msg.submit(predict, [msg, chat_bot, keep_thinking], [msg, chat_bot,])

demo.launch()
