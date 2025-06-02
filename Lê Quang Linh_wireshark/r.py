import pyshark
path = r"D:\Data\Learn 3n2\Nets_and_num_trans\data16A2020425.pcapng"

cap = pyshark.FileCapture(path, display_filter='http')

print("Phân tích gói tin HTTP REQUEST chứa từ khóa 'login' hoặc 'test'\n")

for i, pkt in enumerate(cap):
    try:
        # Chuyển toàn bộ nội dung HTTP sang dạng chữ thường để tìm kiếm dễ hơn
        http_info = str(pkt.http).lower()
        # Nếu trong nội dung gói có chứa 'login' hoặc 'test'
        if 'login' in http_info or 'test' in http_info:
            print("="*50)
            print(f"GÓI #{i+1} Có chứa từ khóa")
        # Hiển thị thời gian bắt được gói tin
        print("Thời gian:", pkt.sniff_time)
        # Hiển thị IP nguồn (máy gửi request) và IP đích (máy chủ)
        print("IP nguồn:", pkt.ip.src if hasattr(pkt, 'ip') else 'N/A')
        print("IP đích:", pkt.ip.dst if hasattr(pkt, 'ip') else 'N/A')
        # Hiển thị phương thức HTTP: GET hoặc POST
        if hasattr(pkt.http, 'request_method'):
            print("Phương thức:", pkt.http.request_method)
        # Hiển thị URL đầy đủ nếu có
        if hasattr(pkt.http, "host") and hasattr(pkt.http, "request_uri"):
            print("URL:", f"http://{pkt.http.host}{pkt.http.request_uri}")
        if hasattr(pkt.http, "cookie"):
            print("Cookie:", pkt.http.cookie)
        if hasattr(pkt.http, "file_data"):
            print("File Data:", pkt.http.file_data)
        
    except Exception as e:
        print("Lỗi:", e)
