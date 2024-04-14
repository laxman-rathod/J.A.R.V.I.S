import platform
import psutil
from jarvis_speech_recognizer import speak
import socket

hostname = socket.gethostname() # Get the hostname of the computer
ip_address = socket.gethostbyname(hostname) # Get the IP address of the computer

def system_information():      
    # System Information
    system_info = {
        'OS': platform.system(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Architecture': platform.machine()
    }

    # CPU Information
    cpu_info = {
        'CPU Count': psutil.cpu_count(),
        'CPU Frequency': psutil.cpu_freq().current,
        'CPU Usage': psutil.cpu_percent(interval=1)
    }

    # Memory Information
    memory_info = {
        'Total Memory': psutil.virtual_memory().total,
        'Available Memory': psutil.virtual_memory().available,
        'Used Memory': psutil.virtual_memory().used,
        'Free Memory': psutil.virtual_memory().free
    }

    # Disk Information
    disk_info = {
        'Disk Usage': psutil.disk_usage('/').used,
        'Disk Partitions': psutil.disk_partitions()
    }
    speak("Sir, here are system's all information")

    # Display System Information
    speak("System Information:")
    
    speak(f"Computer name: {hostname}")
    speak(f"IP Address: {ip_address}")

    for key, value in system_info.items():
        speak(f"{key}: {value}")

    # Display CPU Information
    speak("\nCPU Information:")
    for key, value in cpu_info.items():
        speak(f"{key}: {value}")

    # Display Memory Information
    speak("\nMemory Information:")
    for key, value in memory_info.items():
        speak(f"{key}: {value}")

    # Display Disk Information
    speak("\nDisk Information:")
    for key, value in disk_info.items():
        speak(f"{key}: {value}")