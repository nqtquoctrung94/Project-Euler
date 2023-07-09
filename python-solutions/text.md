Chúng ta có thể phân tích một số thành tích của các số nguyên tố, sau đó dựa vào tính chất sau:

Gọi $p$ là số nguyên tố
- Số lượng ước số của $p$, $\sigma_{0}{(p)} = 2$, tổng ước số là $\sigma_{1}{(p)} = p+1$
- Số lượng ước số của $p^k$, $\sigma_{0}{(p^k)} = k +1$, tổng ước số là $\sigma_{1}{(p^k)} = \frac{p^{k+1}-1}{p-1}$
    - Chứng minh:
        - Các ước số của $p^k$ lần lượt là $1, p, p^2, p^3,\dots,p^k$ 
        - Hay $p^0, p^1, p^2,\dots,p^k$ 
        - Vậy:
            - Ta có k+1 ước số
            - Tổng các ước số = $p^0 + p^1 + p^2 + \dots + p^k = \frac{p^{k+1}-1}{p-1} $ 
            
Một số phân tích thành tích của $p_{1}^{m}$ và $p_{2}^{n}$, ta có:
- Số lượng ước số:
    $\sigma_{0}{(p_{1}^{m} \times p_{2}^{n})} = \sigma_{0}{(p_{1}^{m})} \times \sigma_{0}{(p_{2}^{n})} = (m+1)\times(n+1)$
- Tổng ước số
    $\sigma_{1}{(p_{1}^{m} \times p_{2}^{n})} = \sigma_{1}{(p_{1}^{m})} \times \sigma_{1}{(p_{2}^{n})} = \frac{p_{1}^{m+1}-1}{p_{1}-1}\times\frac{p_{2}^{n+1}-1}{p_{2}-1}$ <br>
    Điều này chứng minh được vì ước chung lớn nhất của $p_{1}$ và $p_{2}$ là $gcd(p_{1},p_{2}) = 1$