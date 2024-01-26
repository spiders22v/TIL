import tkinter as tk
from tkinter import ttk
import subprocess

def generate_dockerfile():
    selected_framework = framework_listbox.get(tk.ACTIVE)
    image_name = f"{selected_framework.lower()}" if selected_framework else "" # 선택된 프레임워크에 따라 이미지 이름 동적으로 생성

    port_mapping = port_entry.get()
    volume_mapping = volume_entry.get()
    env_variables = env_entry.get()

    # 디폴트로 추가되는 도커파일 부분
    dockerfile_content = f"FROM {image_name}\n" if image_name else ""
    dockerfile_content += "EXPOSE " + port_mapping + "\n" if port_mapping else ""
    dockerfile_content += "VOLUME " + volume_mapping + "\n" if volume_mapping else ""
    dockerfile_content += "ENV " + env_variables + "\n" if env_variables else ""
    dockerfile_content += "RUN pip install matplotlib scikit-learn\n"
    dockerfile_content += "EXPOSE 8888\n"
    dockerfile_content += 'CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]\n'

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, dockerfile_content)

def build_docker_image():
    dockerfile_content = result_text.get(1.0, tk.END)
    with open("Dockerfile", "w") as dockerfile:
        dockerfile.write(dockerfile_content)

    subprocess.run(["docker", "build", "-t", "custom-docker-image", "."])

def add_framework():
    new_framework = new_framework_entry.get()
    framework_listbox.insert(tk.END, new_framework)

def delete_framework():
    selected_index = framework_listbox.curselection()
    if selected_index:
        framework_listbox.delete(selected_index)

def close_application():
    root.destroy()

# GUI 생성
root = tk.Tk()
root.title("Dockerfile Generator")

# 프레임워크 선택 (리스트 박스)
framework_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
framework_listbox.insert(tk.END, "pytorch/pytorch:latest")
framework_listbox.insert(tk.END, "pytorch/pytorch:2.1.2-cuda11.8-cudnn8-devel") 
framework_listbox.insert(tk.END, "pytorch/pytorch:2.1.2-cuda11.8-cudnn8-runtime") 
framework_listbox.insert(tk.END, "pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel") 
framework_listbox.insert(tk.END, "pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime") 
framework_listbox.insert(tk.END, "tensorflow/tensorflow:latest")
framework_listbox.insert(tk.END, "tensorflow/tensorflow:latest-jupyter")
framework_listbox.insert(tk.END, "tensorflow/tensorflow:latest-gpu")
framework_listbox.pack(pady=10)

# 새로운 프레임워크 추가 입력 상자 및 버튼
new_framework_label = tk.Label(root, text="New Framework:")
new_framework_label.pack(pady=5)

new_framework_entry = ttk.Entry(root)
new_framework_entry.pack(pady=5)

add_framework_button = tk.Button(root, text="Add Framework", command=add_framework)
add_framework_button.pack(pady=5)

delete_framework_button = tk.Button(root, text="Delete Selected", command=delete_framework)
delete_framework_button.pack(pady=5)

# 포트 매핑
tk.Label(root, text="Port Mapping:").pack(pady=5)
port_entry = ttk.Entry(root)
port_entry.pack(pady=5)

# 볼륨 매핑
tk.Label(root, text="Volume Mapping:").pack(pady=5)
volume_entry = ttk.Entry(root)
volume_entry.pack(pady=5)

# 환경 변수
tk.Label(root, text="Environment Variables:").pack(pady=5)
env_entry = ttk.Entry(root)
env_entry.pack(pady=5)

# 도커파일 미리보기 및 생성 버튼
tk.Button(root, text="Generate Dockerfile", command=generate_dockerfile).pack(pady=10)

# 도커파일 미리보기 창
tk.Label(root, text="Generated Dockerfile:").pack(pady=5)
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

# 도커 이미지 빌드 버튼
tk.Button(root, text="Build Docker Image", command=build_docker_image).pack(pady=10)

# 종료 버튼
tk.Button(root, text="Close", command=close_application).pack(pady=10)

root.mainloop()
