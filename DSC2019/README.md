## text 처리
- 문자 -> 숫자 변환(vector 등)
    - word를 vector로 변환, document를 vector로 변환 등
    - bag of words
        - word dictionary를 만든 후, word의 순서를 고려하지 않고 count만 고려하여 vectorize 하는 방법
        - integer 값을 갖는 vector
    - word embedding
        - 다양한 방법으로(embedding에 여러가지 방법이 있음) word를 real-number vector화 하는 방법
        - vector간의 연산이 가능함
            - ex) <img src='./imgs/equation_3.png'>
    - data가 적은 경우에는 bag of words, tf-idf 등의 방법도 충분히 잘 됨
        - 단 data가 많아질수록 word embedding이 잘됨

- 유사하다의 정의(== vector의 유사도 정의)
    - euclid distance
        - 두 벡터 사이의 거리
        - aka L2 norm of vector
        - <img src='./imgs/equation_1.png'>
    - cosine similarity
        - cosine 값을 이용한 similarity
        - <img src='./imgs/equation_2.png'>
    - text 관련 문제에서는 cosine similarity를 많이 씀
        - 방향에 대한 고려 가능
            - ex) s1 = 'Love Love Love', s2 = 'Love Love Hate', s3 = 'Love Love' 에서 s2보다 s3가 s1과 더 유사하다고 판단할 수 있음

## pandas 기본
- tabular data를 다루기위한 library(2d data)
- deep learning은 image, sound 등의 비정형 data를 주로 다루고 machine learning은 tabular data를 주로 다룸
- groupby() => sum 등의 aggregation 함수와 같이 사용
- map() => Series의 각 element에 적용
- apply() => Series에 aggregation 적용
- merge() => DB에서의 Join과 똑같음


## data 전처리
- 결측치 관리 / scale 관리 / label data 처리 등 실제 model을 적용하기 전에 수행하는 전처리
- 결측치 관리
    - drop
        - 해당 row나 column을 drop함
        - df.dropna() 등
    - fill
        - mean(평균), median(중앙값), mode(최빈값) 등으로 채움
        - groupby 등을 이용해서 해당 group의 통계치를 이용하여 채우는 것도 고려
        - df.fillna() 등
- label data 처리
    - onehot encoding
        - pd.get_dummies() 이용
        - sklearn의 LabelEncoder, OneHotEncoder 이용
        - keras의 to_categorical() 등 다양한 선택지 있음
    - embedding
        - onehot encoding은 보통 매우 sparse하므로 feature로 사용할 때에는 embedding을 이용하여 차원 축소
        - word2vec, node2vec, svd 등 이용
    - binning
        - range value를 categorized value로 바꾸는 것
        - pd.cut() 등 이용
- scaling
    - 값의 scale을 고려하여 새로운 값으로 바꿔줌
    - 원래의 분포를 유지한 채 값의 크기만 바꿔줌
    - sklearn에 다양한 Scaler가 있음

## MISC
- os.path.join을 사용하는 이유
    - window와 mac/linux에서 path seperator가 다름
        - widnow: \
        - mac, linux: /
- matplotlib
    - plt.plot() => fig에 그림 그리기
    - plt.show() => fig에 있는 그림 flush
    - fig => 그림을 그리는 판
    - add_subplots() 등을 통해서 fig를 나눌 수 있음