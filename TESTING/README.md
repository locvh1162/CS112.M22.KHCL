# KIỂM TRA TÍNH ĐÚNG ĐẮN & HIỆU NĂNG CỦA CHƯƠNG TRÌNH BẰNG BỘ TEST

## Tính đúng đắn và hiệu năng của CT?

- **Tính đúng đắn** của CT được thể hiện khi CT thực hiện chính xác những mục tiêu và chức năng đã được đề xuất ở giai đoạn thiết kế.
- Tính đúng đắn của CT được xác xác định bằng:
    - Tính đúng đắn của thuật toán.
    - Tính tương đương của chương trình với thuật toán: Thuật toán đúng nhưng lập trình sai sẽ dẫn đến kết quả sai.
- **Hiệu năng** thực hiện 1 chương trình chủ yếu phụ thuộc vào 4 yếu tố:
    - Tốc độ của CPU
    - Số nhân của CPU (khả năng thực hiện chạy song song đa luồng)
    - Thuật toán
    - Kích thước bộ dữ liệu
- Kiểm tra tính đúng đắn và hiệu năng là hành động mà chúng ta gọi là **TEST**

## Automated Testing vs. Manual Testing

### Manual testing (Test thủ công)

- **Manual testing**:
    - Liệt kê các tính năng, hàm của CT
    - Liệt kê các dữ liệu vào có thể chấp nhận và kết quả mong đợi
    - Chạy thử chương trình xem có ra kết quả mong đợi hay không
- **Hạn chế**:
    - Khi cần thay đổi code thì phải check lại các hàm đã liệt kê và kiểm tra từng hàm (nếu như chương trình có nhiều hàm)
    
### Automated Testing (Test tự động)

- **Automated Testing** là việc thực hiện test plan mà mình đã lập ra.
- Test bằng các test case, test script thay vì con người.
- Test case, script phải chỉ định rõ dữ liệu vào, các bước thực hiện và dữ liệu mong chờ sẽ xuất ra.

## Unit Test vs. Integration Test

### Integration Test (Test tích hợp)

- **Integration Test** là kiểm tra tất cả cách thành phần của chương trình 1 lúc
- **Hạn chế**: Khi chương trình bị sai phải dò lại từng hàm để tìm lỗi.

### Unit test (Test thành phần)

- **Unit Test** là test 1 thành phần nhỏ của cả chương trình.
- 1 Unit có thể là 1 hàm (function), 1 lớp (class), hoặc 1 phương thức (method),...
- **Lợi ích khi sử dụng Unit Test**:
    - Dễ test khi thay đổi code của chương trình.
    - Cách ly được những hàm bị lỗi, dễ xác định nguyên nhân và khắc phục, tiết kiệm chi phí và thời gian.
    - Phát hiện được những hàm chạy chậm, không hiệu quả thông qua thời gian chạy của unit test.
    
## Unit Test với Python

- Lấy ví dụ với hàm sum(), được xây dựng sẵn trong Python dùng để tính tổng các số.

- Để viết Unit test cho hàm sum(), ta sẽ kiểm tra output của sum() so với output cho trước, ở đây là 6.

```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

- Thực thi đoạn code trên sẽ không cho ra kết quả gì, vì 1 + 2 + 3 đã đúng bằng 6.

- Nếu kết quả từ sum() không chính xác, thì test sẽ fail với một AssertionError và sẽ hiển thị "Should be 6" khi thực thi:

```python
assert sum([1, 1, 1]) == 6, "Should be 6"
```

- Kết quả thực thi:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be 6
```

- Ta đưa cả 2 test case vào 1 file `test.py`:

```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_2():
    assert sum([1, 1, 1]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_2()
    print("Everything passed")
```

- Kết quả thực thi:

```
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    test_sum_2()
  File "test.py", line 5, in test_sum_2
    assert sum([1, 1, 1]) == 6, "Should be 6"
AssertionError: Should be 6
```

- `assert` là cách đơn giản nhất để viết 1 test case. Nhưng cách thông dụng nhất thì là sử dụng module **unittest** có sẵn trong standard library.

## Module unittest

- **unittest** có 1 số yêu cầu quan trọng để viết và thực thi test:
    - Các test được cần đặt trong class như các phương thức.
    - Sử dụng các phương thức assertion đặc biệt của lớp `unittest.TestCase` thay cho lệnh assert ở trên.

> Các bước viết test case bằng unittest:
>   1. `import unittest` từ standard library
>   2. Tạo 1 lớp mới kế thừa từ lớp `TestCase`
>   3. Chuyển các test function thành các phương thức của lớp bằng cách thêm `self` làm đối số đầu tiên
>   4. Thay các lệnh `assert` bằng các phương thức assertion của lớp `TestCase`
>   5. Thay command-line entry point để gọi `unittest.main()`

- Bằng các bước vừa nêu, ta thay đổi file `test.py` bằng `test2.py`:

```python
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_2(self):
        self.assertEqual(sum([1, 1, 1]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

- Thực thi chương trình ta sẽ thấy 1 test thành công (kí hiệu dấu .), 1 test thất bại (kí hiệu chữ F).

```
.F
======================================================================
FAIL: test_sum_2 (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test2.py", line 9, in test_sum_2
    self.assertEqual(sum([1, 1, 1]), 6, "Should be 6")
AssertionError: 3 != 6 : Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

### Các phương thức assertion của module unittest

|Phương thức|Tương đương với|
|---|---|
|.assertEqual(a, b)|a == b|
|.assertTrue(x)|	bool(x) is True|
|.assertFalse(x)|	bool(x) is False|
|.assertIs(a, b)|	a is b|
|.assertIsNone(x)|	x is None|
|.assertIn(a, b)|	a in b|
|.assertIsInstance(a, b)|	isinstance(a, b)|

- .assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() đều có các phương thức đối lập là assertIsNot.(),...

## Black Box Testing vs. White Box Testing

![blackwhite](https://uploads-ssl.webflow.com/5c8ff8ef21fa8e5620d8a48e/5f953043a15dd424f61b332e_black%20and%20white%20box.jpg)

### Black Box Testing 

![blackbox](https://images.viblo.asia/e7e35f73-35fe-4351-90a5-121f6b0de237.jpg)

- Là phương pháp test không quan tâm cấu trúc chương trình.
- Yêu cầu phải viết test case đầy đủ trước khi test; khi test, đơn giản chỉ cần thực hiện theo các bước mô tả trong test case thao tác và nhập data vào, sau đó xem kết quả trả về hoặc hành vi của phần mềm, rồi so sánh với kết quả mong đợi được viết trong testcase.
> - **Khi viết test case**: Dựa vào yêu cầu và giao diện bên ngoài của chương trình (Không can thiệp vào bên trong code của chương trình)
> - **Khi thực hiện test**: Thực hiện trên giao diện của chương trình (yêu cầu chương trình phải chạy được mới test được, không can thiệp vào code)

### White Box Testing

![whitebox](https://ecomputerconcepts.com/wp-content/uploads/2021/01/White-box-testing.jpg)

- Là phương pháp test yêu cầu phải biết cấu trúc bên trong của chương trình.
- Yêu cầu phải viết test case đầy đủ các nhánh trong code; khi test, sẽ set điều kiện và data để chạy vào đủ tất cả các nhánh trong giải thuật, đảm bảo thực hiện đầy đủ.
> - **Khi viết test case**: Dựa vào yêu cầu và nội dung Source Code (can thiệp vào bên trong Code của chương trình)
> - **Khi thực hiện test**: Thực thi test trong code (không cần thực thi chương trình, vì thực hiện test white box sẽ sử dụng framework nào đó hỗ trợ (Ví dụ như test kiểu debug)

## Kết luận: Cách tạo 1 bộ test

- Trước khi tạo 1 bộ test, bạn cần biết mình test cái gì.
- Sau đó thực hiện 3 bước cở bản:
>    1. Tạo input.
>    2. Chạy code, lưu lại output của code.
>    3. **Assertion**: So sánh output với kết quả mong muốn.



    

