def solution(tri):
    """ 
    주어진 삼각형 구조의 배열에서 이동가능한 곳으로 이동 후 최댓값이 되는 값을 저장
    
    전략 : triangle 배열과 같은 사이즈의 dp 배열을 만들고, 해당 값을 지나는 숫자의 합 중 최댓값을 갱신 
    
    i번째 칸에서 j번째 값은 -> i+1번째 칸의 j and j+1 으로만 이동 가능
    ex) [0][0] -> [1][0], [1][1] 
    """
    n = len(tri)
    def tri_dp(tri): 
        dp = [[0]*(i+1) for i in range(n)]
        dp[0][0] = tri[0][0]
        
        for i in range(n-1): 
            for j in range(i+1): 
                dp[i+1][j] = max(dp[i+1][j], dp[i][j]+tri[i+1][j]) # 대각선 좌 
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+tri[i+1][j+1]) # 대각선 우
        
        return max(dp[-1])
                
    return tri_dp(tri)