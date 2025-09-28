# Leave Request Email Filter

## Mô tả
Script `filter_leave_requests.py` lọc các email liên quan đến nghỉ phép (leave request) từ file `emails.csv` dựa trên từ khoá "leave" xuất hiện trong subject hoặc body.
- Nếu subject hoặc body chứa từ "leave" (không phân biệt hoa thường), email sẽ được coi là leave request.
- Kết quả xuất ra file `leave_request.json`.


## Case
### Body có từ "leave" nhưng không phải leave request
Ví dụ trong `emails.csv`:

| id  | sender            | subject         | body                                               |
|-----|-------------------|-----------------|----------------------------------------------------|
| 13  | mary@company.com  | Project update  | I will cover for John while he is on leave.        |
| 14  | steve@company.com | HR              | The leave policy will be updated next month.       |
| 15  | anna@company.com  | Leave request   | I am not requesting leave, just confirming my attendance. |

Theo logic cơ bản, các email này vẫn bị lọc là leave request do có từ "leave" trong body hoặc subject. Tuy nhiên, về mặt ngữ nghĩa, đây không phải là yêu cầu nghỉ phép thực sự.


### Email với thông tin không đầy đủ
Email số 6 trong `emails.csv`:

| id  | sender            | subject | body |
|-----|-------------------|---------|------|
| 6   | frank@company.com | Leave   | ""   |

  Subject chỉ có từ "Leave" mà không rõ ý định. Body hoàn toàn trống, có thể là một email lỗi.

## Sử dụng AI để phân tích ngữ nghĩa

### So sánh kết quả Logic cơ bản vs AI Gemini

**Logic cơ bản (leave_request.json):**
- Tổng số email được lọc: 14/15 (loại trừ ID 2 - IT issue không chứa "leave")
- Phương pháp: Tìm kiếm từ khóa "leave" trong subject/body

**AI Gemini (sentiment_results.json):**
- Tổng số email được phân loại là leave request: 7/15
- Phân tích ngữ cảnh và ý định thực sự

### Phân tích chi tiết các case study:

**Case 1: Email có từ "leave" nhưng không phải leave request**

| ID | Email | Logic cơ bản | AI Gemini | Nhận xét |
|----|-------|--------------|-----------|----------|
| 13 | "I will cover for John while he is on leave" |  (lọc vào) |  (not) | chỉ thông báo cover |
| 14 | "The leave policy will be updated" |  (lọc vào) |  (not) | Thảo luận policy |
| 15 | "I am not requesting leave, just confirming" |  (lọc vào) |  (not) | Xác nhận không phải request leave |

**Case 2: Email với thông tin không đầy đủ**

| ID | Email | Logic cơ bản | AI Gemini | Nhận xét |
|----|-------|--------------|-----------|----------|
| 6 | Subject: "Leave", Body: "" |  (lọc vào) |  (not) | thiếu thông tin |

### Kết luận:

- **Hiểu ngữ cảnh**: AI có khả năng phân biệt được ý định thực sự trong email
- **Xử lý edge case**: AI thận trọng hơn với các trường hợp thiếu thông tin
