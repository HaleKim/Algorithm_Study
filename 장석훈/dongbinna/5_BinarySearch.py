'''

## 1. 이진 탐색

* **정의**: 정렬된 배열에서 절반씩 범위를 좁혀 가며 원하는 값을 찾는 탐색 기법
* **전제 조건**: 반드시 ‘오름차순’(혹은 내림차순) 정렬돼 있어야 함

## 2. 기본 흐름 (의사코드)

'''
left ← 0
right ← n - 1

while left ≤ right:
    mid ← (left + right) // 2
    if array[mid] == target:
        return mid         # 찾았을 때 인덱스 반환
    elif array[mid] < target:
        left ← mid + 1     # 오른쪽 절반으로 이동
    else:
        right ← mid - 1    # 왼쪽 절반으로 이동

return -1                    # 못 찾으면 -1 반환
'''

## 3. 구현 시 주의사항

* **중간 인덱스 계산**

  * `(left + right) // 2`
  * (자바/C++에서 오버플로우 우려 시) `left + (right - left) // 2`
* **반복 종료 조건**

  * `left > right` 일 때 루프 탈출
* **무한 반복 방지**

  * `mid` 계산 후, 반드시 `left` 또는 `right` 가 이동하도록

## 4. 재귀 vs 반복

* **반복형 (while)**

  * 메모리/스택 부담 적고 속도 빠름
* **재귀형**

  ```python
  def binary_search(arr, target, l, r):
      if l > r:
          return -1
      m = (l + r) // 2
      if arr[m] == target:
          return m
      elif arr[m] < target:
          return binary_search(arr, target, m+1, r)
      else:
          return binary_search(arr, target, l, m-1)
  ```

  * 코드가 간결하나, 깊은 재귀 주의

## 5. 응용: 경계 탐색 (lower\_bound/upper\_bound)

* **lower\_bound**: `값 ≥ target`인 첫 위치
* **upper\_bound**: `값 > target`인 첫 위치
* 구현 포인트:

  * `while left < right:`
  * `mid = (left + right) // 2`
  * 조건에 따라 `right = mid` 또는 `left = mid+1`

## 6. 시간/공간 복잡도

* **시간**: O(log n)
* **공간**:

  * 반복형 O(1)
  * 재귀형 O(log n) (재귀 스택)

## 7. 대표 문제 유형

1. **정수 탐색**: 단순 값 존재 여부
2. **최댓값/최솟값 찾기**: 배열 정렬 후 활용
3. **조건 만족 구간 탐색**: “최대 k 이하인 요소 개수” 등
4. **이분 탐색 응용**: 파라메트릭 서치(결정 문제 + 이진 탐색)

---

이 구조대로 각각의 구현 포인트와 예제를 차례로 따라가기.

'''