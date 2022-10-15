while True:    #循环1
  try:
     N=int(input('Enter an interger:'))
     n=2
     j=0
     if N>=3:
        print('The prime numbers smaller than %s include:'%N)
        while n<N:   #输出质数,循环3
           i=2
           t=1
           while i<n:
              if n%i==0:
                  t=0
              i+=1
           if t!=0:
              j+=1
              if j%8==0:
                  print(n,end=' \n')
              else:
                  print(n,end=' ')
           n+=1
        break    #结束循环1
     else:
         print(f'There is no prime number smaller than {N}')
         continue  #回到开端,重新进行循环1         
  except:
    print('You did not enter a valid input')


            
