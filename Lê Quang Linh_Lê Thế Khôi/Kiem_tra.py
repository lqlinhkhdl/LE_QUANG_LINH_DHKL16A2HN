import pyshark

# Đường dẫn đến file pcapng đã lưu
path = r'D:\Data\Learn 3n2\Nets_and_num_trans\New Folder\newdata.pcapng'

cap = pyshark.FileCapture(path, display_filter = 'http.request')

print("Phân tích gói HTTP REQUEST chứa từ khoá 'login' hoặc'test'\n")

# Duyệt qua từng gói tin trong file
for i, pkt in enumerate(cap):
    try:
        # Chuyển toàn bộ nội dung HTTP sang dạng chữ thường để tìm kiếm dễ hơn
        http_info = str(pkt.http).lower()
        # Nếu trong nội dung gói có chứa 'login' hoặc 'test'
        if 'login' in http_info or 'test' in http_info:
            print("="*50)
            print(f"GÓI #{i+1} Có chứa từ khoá")
            # Hiển thị thời gian bắt được gói tin
            print("Thời gian:", pkt.sniff_time)
            # Hiển thị IP nguồn (máy gửi request) và IP đích (máy chủ)
            print("IP nguồn:", pkt.ip.src if hasattr(pkt, 'ip')
        else 'N/A')
            print("IP đích:", pkt.ip.dst if hasattr(pkt, 'ip')
        else 'N/A')
        # Hiển thị phương thức HTTP: GET hoặc POST
        if hasattr(pkt.http, 'request_method'):
            print("Phương thức:", pkt.http.request_method)
        # Hiển thị URL đầy đủ nếu có
        if hasattr(pkt.http, 'host') and hasattr(pkt.http,'request_uri'):
            print("URL:",f"http://{pkt.http.host}{pkt.http.request_uri}")
            # Hiển thị Cookie nếu gói có gửi cookie
            if hasattr(pkt.http, 'cookie'):
                print("Cookie:", pkt.http.cookie)
            # Hiển thị dữ liệu gửi đi trong phần thân (POST form data)
            if hasattr(pkt.http, 'file_data'):
                print("Payload:", pkt.http.file_data)
            # Nếu có lỗi (ví dụ gói tin không có lớp http), thì tiếp tục gói sau
    except Exception as e:
        print(f"[Lỗi tại gói #{i+1}]: {e}")