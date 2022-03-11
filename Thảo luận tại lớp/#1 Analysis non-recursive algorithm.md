# PHÂN TÍCH ĐỘ PHỨC TẠP THUẬT TOÁN KHÔNG ĐỆ QUY

- Độ phức tạp lưu trữ: dung lượng bộ nhớ cần thiết
- Độ phức tạp tính toán: TG chiếm dụng CPU nhiều hay ít => đo số phép toán CPU cần dùng để xử lý

## XÁC ĐỊNH ĐỘ PHỨC TẠP BẰNG LÝ THUYẾT

Đếm số phép toán cơ sở (đại lượng tương đương là số lần lặp):
1. Đếm số vòng lặp
2. Đếm số phép so sánh/ phép gán rồi nhân số vòng lặp
3. Làm sấp xỉ bằng cách bỏ hệ số

## Big O, big Omega, big Theta

### Big O:

#### Định nghĩa
Giả sử f(n) và g(n) là các hàm thực không âm của đối số nguyên không âm n. Ta nói "g(n) là O của f(n)" và viết là: `(n) = O(f(n))`nếu tồn tại các hằng số dương C và n0 sao cho `(n) <= C * f(n)` với mọi `n >= n0`

<p align="center">
  <a style="border: none;">
    <img src="https://images.viblo.asia/85e5d30d-9bbf-462f-be31-83511240ad5a.png" alt="bigo" style="width:30%;height:30%;">
  </a>
</p>

#### Cách tính
Độ phức tạp tính toán của giải thuật: O(f(n))

- Việc xác định độ phức tạp tính toán của giải thuật trong thực tế có thể tính bằng một số quy tắc đơn giản sau:

1. Quy tắc bỏ hằng số:
>           T(n) = O(c.f(n)) = O(f(n)) với c là một hằng số dương

2. Quy tắc lấy max:
>                   T(n) = O(f(n)+ g(n)) = O(max(f(n), g(n)))

3. Quy tắc cộng:
>           T1(n) = O(f(n))         T2(n) = O(g(n))
>           T1(n) + T2(n) = O(f(n) + g(n))

4. Quy tắc nhân:
>           Đoạn chương trình có thời gian thực hiện T(n)=O(f(n))
>           Nếu thực hiện k(n) lần đoạn chương trình với k(n) = O(g(n)) thì độ phức tạp sẽ là O(g(n).f(n))

<p align="center">
  <a style="border: none;">
    <img src="https://itzone.com.vn/wp-content/uploads/2020/06/96851ae4-1258-4f5e-97ac-2a6a1d23e6fc.png" alt="bigO" style="width:50%;height:50%;">
  </a>
</p>

### Big Omega, Big Theta

- Tương tự như Big O, nếu như tìm được các hằng số C, k1, k2 đều dương, không phụ thuộc vào n, sao cho với các số n đủ lơn, các hàm R(n), f(n) và h(n) đều dương và `R(n) >= C.f(n)` va `k1.h(n) =< R(n) <= k2.h(n)` thì ta nói thuật toán có độ phức tạp cỡ lớn hơn Omega(f(n)) và đúng bằng cỡ Theta(h(n))
- Chúng ta có thể hiểu Big(O), Omega, Theta như những hàm tiềm cận của hàm tính độ phức tạp của thuật toán.

<p align="center">
  <a style="border: none;">
    <img src="https://images.viblo.asia/16c03bbc-e8d7-488f-8b1a-89546a2e6031.png" alt="theta" style="width:30%;height:30%;">
  </a>
</p>

<p align="center">
  <a style="border: none;">
    <img src="https://images.viblo.asia/f293e4dc-371f-42f7-b295-77e056e06ec0.png" alt="omega" style="width:30%;height:30%;">
  </a>
</p>
