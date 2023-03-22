M, N, K = map(int,input().split())
lst_m = list(map(int, input().split()))
lst_n = list(map(int, input().split()))
if M > N:
    print("normal")
else:
    cnt = 0
    for i in range(0, N - M + 1):
        cnt += 1
        if lst_n[i:i+M] == lst_m:
            print("secret")
            break
        if cnt == N - M + 1:
            print("normal")

    