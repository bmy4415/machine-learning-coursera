# 01. learning_prob
- Learning from data의 조건
    - explicit한 수학적 modeling이 어려움 => 만약 가능하면 그것으로 모델링하면 됨
    - empirical modeling을 위한 충분한 data가 있어야함
    - 정리: 매우 복잡해서 수학적인 modeling은 어렵지만 충분한 data가 있어서 `자동`으로 학습하는것이 가능한 경우 `Learning from data`가 가능함
    - 예시
        1. 주어진 자연수에 대해서 소수 판별 => 수학적 modeling 가능
        2. 높이 h에서 자유낙하한 물체가 지면에 도달할 때까지 걸리는 시간 => 수학적 modeling 가능(물론 수많은 data로부터 학습도 가능)
        3. 신용카드 사용 패턴으로부터 이상행동 감지 => 수학적으로 modeling하기 어려움
- Perceptron
    - 하나의 계산 component
    - 주어진 ![equation](https://latex.codecogs.com/gif.latex?x%5Cin%20%7B%20R%20%7D%5E%7B%20d%20%7D%2Cw%5Cin%20%7B%20R%20%7D%5E%7B%20d%20%7D)에 대해서 ![equation](https://latex.codecogs.com/gif.latex?x%5Ccdot%20w)로 계산(weighted sum)
    - 이때 w와 x의 관계가 `linear`함
- learning model의 구성 요소
    - hypothesis => 실제 예측 모델
        - 예를들어 1차원 regression 문제에서 `y=ax+b로 예측하는 수식`
    - learning algorithm => hypothesis 중 가장 optimal한 것을 찾는 방법
        - 위의 `y=ax+b`에서 optimal한 a와 b를 찾는 과정
        - PLA(Perceptron Learning Algorithm)
            - learning algorithm의 한가지 방법
            - train data, train label(![equation](https://latex.codecogs.com/gif.latex?%7B%20x%20%7D_%7B%20i%20%7D%2C%7B%20y%20%7D_%7B%20i%20%7D)), hypothesis(![equation](https://latex.codecogs.com/gif.latex?h%28x%29%3Dsign%28wx%29)) 일 때 임의의 mis-classify한 example에 대해서(![equation](https://latex.codecogs.com/gif.latex?h%28x%29%3Dsign%28w%7B%20x%20%7D_%7B%20i%20%7D%29%5Cneq%20%7B%20y%20%7D_%7B%20i%20%7D)) ![equation](https://latex.codecogs.com/gif.latex?w%3Dw&plus;%7B%20y%20%7D_%7B%20i%20%7D%7B%20x%20%7D_%7B%20i%20%7D) 수행
            - y=1인 경우, w와 x의 cosine값을 줄이는 방향으로 update
            - y=-1인 경우, w와 x의 cosine값을 키우는 방향으로 update
            - 주어진 data과 linearly separable하지 않으면 iteration이 끝나지 않음
- machine learning problem 종류
    - 크게 supervised / unsupervised / reinforce의 3가지 종류
    - correct label(정답)의 유무
        - supervised: correct label 존재
        - unsupervised: correct label 존재하지 않음
        - reinforce: correct label은 없지만 possible label이 있고 해당 label에 대하여 평가(grade) 가능 => 평가가 가장 좋은 방법을 계속 찾도록 함
    - 주요 problem
        - supervised
            - regression(real value 예측)
            - classification(discrete value 예측)
        - unsupervised
            - clustering ex) k-means 등
            - feature extraction(PCA, SVD 등)
                - label은 없지만 clustering의 경우 비슷한 것들을 비슷한 vector로 나타내면 feature extraction의 효과가 있음
        - reinforcement
            - 가능한 action과 그에 대한 grade를 통해 학습하는 환경 ex) AlphaGo, Auto mobile

# 02. feasibility_learning
- learning의 목표: f라는 unknown function을 알아내야함, 그러나 unseen data에 있는 어떤 성질까지 완벽히 알아내는 것은 `불가능` => `probabilistic way`로 f와 최대한 비슷한 g를 알아내보자
- red와 green공이 들어있는 항아리에서 공을 뽑을때 어떤 색깔이 뽑힐지 예측하기
    - 한두번 뽑아보는 것으로 예측하기 어렵지만 충분히 여러번 `독립적으로` 뽑아보면 red공이 나올 `probabilty`를 구할 수 있음
- Hoefdding Inequality
    - |<실험을 통해 계산한 probability> - <실제 probability>|가 upper bound K를 갖는데, K는 <실험 횟수>가 커질수록 작아짐(![equation](https://latex.codecogs.com/gif.latex?K%5Cpropto%20%7B%20e%20%7D%5E%7B%20-N%20%7D))
    - **즉 충분히 실험을 많이 하면(sample을 많이 뽑으면) ground truth에 근사한 function g를 알아낼 수 있음**
- in-sample vs out-sample:
    - in-sample: random but can calculate
    - out-sample: fixed but cannot calculate
- Ein: in-sample error, Eout: out-sample error
- Machine Leanring의 목표: Eout -> 0
    - 그러나 실제로는 불가능(unseen data에 대해서 Eout을 측정조차 할 수 없음)
    - Hoefdding Inequality에서 |Ein - Eout|이 N에 의해서 upper bound가 정해지므로 다음의 2가지를 해결해보자
        1. |Ein - Eout|을 0에 가깝게 만들자(train error ~= test error로 만들자)(== generalization)
        2. Ein을 0에 가깝게 만들자(train error를 0으로 만들자)(== approximation)
        - 1과 2를 동시에 만족하면 Eout이 0이 된다!
        - 그러나 1과 2는 trade off가 있음
            - model의 complexity를 올리면 Ein이 0에 가까워지지만 |Ein - Eout|이 커짐(over fitting)
            - model의 complexity를 낮추면 |Ein - Eout|이 0에 까까워지지만 Ein이 커짐(under fitting)
- error
    - 실제 f와 우리의 hypothesis h의 차이를 measure하는 방법
    - `error measure`를 어떻게 하는지가 매우 중요!
    - False Positive vs False Negative는 문제에 따라 중요도가 다름 => **정하기가 어려우면 유명한/빈번히 쓰이는 meauser을 쓰자!**
- noise
    - error와는 다른 개념으로 f에 naturally 섞여 있는것
    - 같은 input x에 대해서 다른 결과 y가 나오게함
    - **f는 determinstic이 아니라 probabilistic함!**
