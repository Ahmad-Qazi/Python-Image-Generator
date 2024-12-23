# import tkinter as tk
# import customtkinter as ctk 
# from PIL import ImageTk
# from authtoken import auth_token
# import torch
# from torch import autocast
# from diffusers import StableDiffusionPipeline 
# app = tk.Tk()
# app.geometry("532x632")
# app.title("Stable Bud") 
# ctk.set_appearance_mode("dark") 
# prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white") 
# prompt.place(x=10, y=10)
# lmain = ctk.CTkLabel(app, height=512, width=512)
# lmain.place(x=10, y=110)
# modelid = "CompVis/stable-diffusion-v1-4"
# device = "cuda"
# pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16,use_auth_token=auth_token) 
# pipe.to(device) 
# def generate(): 
#     with autocast(device): 
#         image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
#     image.save('generatedimage.png')
#     img = ImageTk.PhotoImage(image)
#     lmain.configure(image=img) 
# trigger = ctk.CTkButton(height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue", command=generate) 
# trigger.configure(text="Generate") 
# trigger.place(x=206, y=60) 
# app.mainloop()













import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline
import torch
auth_token = "your_hugging_face_auth_token"
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)
lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16" if device == "cuda" else "main", torch_dtype=torch.float16 if device == "cuda" else torch.float32, use_auth_token=auth_token)
pipe.to(device)
def generate():
    user_prompt = prompt.get()
    if not user_prompt.strip():
        print("Please enter a prompt")
        return
    with torch.inference_mode():
        image = pipe(user_prompt, guidance_scale=8.5).images[0]
    image = image.resize((512, 512), Image.LANCZOS)
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)
    lmain.image = img
trigger = ctk.CTkButton(height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue", command=generate)
trigger.configure(text="Generate")
trigger.place(x=206, y=60)
app.mainloop()
