# Leave Request Email Filter

## Mô tả
Script `filter_leave_requests.py` lọc các email liên quan đến nghỉ phép (leave request) từ file `emails.csv` dựa trên từ khoá "leave" xuất hiện trong subject hoặc body.
- Nếu subject hoặc body chứa từ "leave" (không phân biệt hoa thường), email sẽ được coi là leave request.
- Kết quả xuất ra file `leave_request.json`.

## Mở rộng với AI (gợi ý)
Để tăng độ chính xác, có thể tích hợp AI để phân tích ngữ cảnh/ngữ nghĩa, ví dụ:
- Sử dụng HuggingFace transformers (pipeline zero-shot-classification) để phân loại ý định.
- Sử dụng OpenAI API (GPT) để phân tích nội dung và xác định email có phải là yêu cầu nghỉ phép thực sự không.

### Ví dụ mở rộng với HuggingFace transformers:
```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification")
labels = ["leave request", "not leave request"]
result = classifier(email_text, labels)
if result['labels'][0] == "leave request" and result['scores'][0] > 0.7:
    # Xử lý như leave request
```

### Lưu ý
- Cần cài đặt thêm thư viện (`transformers`, `torch`, hoặc đăng ký OpenAI API key nếu dùng GPT).
- Việc tích hợp AI giúp loại bỏ các trường hợp chỉ nhắc đến "leave" nhưng không phải là yêu cầu nghỉ phép thực sự.


## Case Study: Các trường hợp đặc biệt

### 1. Body có từ "leave" nhưng không phải leave request
Ví dụ trong `emails.csv`:

| id  | sender            | subject         | body                                               |
|-----|-------------------|-----------------|----------------------------------------------------|
| 13  | mary@company.com  | Project update  | I will cover for John while he is on leave.        |
| 14  | steve@company.com | HR              | The leave policy will be updated next month.       |
| 15  | anna@company.com  | Leave request   | I am not requesting leave, just confirming my attendance. |

Theo logic cơ bản, các email này vẫn bị lọc là leave request do có từ "leave" trong body hoặc subject. Tuy nhiên, về mặt ngữ nghĩa, đây không phải là yêu cầu nghỉ phép thực sự.

**Giải pháp:**
- Có thể tích hợp AI để phân tích ý định/ngữ cảnh nhằm loại bỏ các trường hợp này.
