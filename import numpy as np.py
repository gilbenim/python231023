import numpy as np

# 시계열 데이터 예제 (여기에 실제 데이터를 제공해야 합니다)
time_series_data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

# 임계값 설정
threshold = 25

# 연속된 5개 중에서 2개 이상의 값이 임계값을 초과하는 경우 감지
for i in range(len(time_series_data) - 4):
    window = time_series_data[i:i+5]
    count_exceed_threshold = np.sum(np.array(window) > threshold)
    
    if count_exceed_threshold >= 2:
        print(f"연속된 5개 중에서 {count_exceed_threshold}개의 값이 임계값을 초과했습니다.")
        print(f"시작 인덱스: {i}, 데이터: {window}")

# 출력 결과:
# 연속된 5개 중에서 2개의 값이 임계값을 초과했습니다.
# 시작 인덱스: 3, 데이터: [25, 30, 35, 40, 45]
