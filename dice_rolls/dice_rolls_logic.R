

# Simulate a dice roll x number of times
# Sum the total of the rolls 
# Any 6's must be rolled again

# Variables
n_rolls <- 1000
dice <- 1:6
rolls_vect <- sample(dice, n_rolls, replace = T)

hist(rolls_vect)

for(roll in 1:n_rolls){
  num <- sample(dice, 1)
  if(num == 6){
    # ...?
  }
}

x <- 6
while(x == 6){
  sample(dice, 1)
  print(x)
}
# INFINITE LOOP!
# x will always be equal to 6

x <- 6
while(x == 6){
  x <- sample(dice, 1)
}
x

test_vect <- vector()
for(test_num in 1:100){
  x <- 6
  while(x == 6){
    x <- sample(dice, 1)
    print(x)
    test_vect[test_num] <- x
  }
}
test_vect
hist(test_vect)

test_vect <- vector()
for(test_num in 1:1000){
  x <- 6
  while(x == 6){
    x <- sample(dice, 1)
    print(x)
    test_vect[test_num] <- x
  }
}
test_vect
hist(test_vect)

rolls_vect <- vector()
for(roll in 1:n_rolls){
  num <- sample(dice, 1)
  if(num == 6){
    while(num == 6){
      num <- sample(dice, 1)
    }
  }
  rolls_vect[roll] <- num
}
rolls_vect
hist(rolls_vect)
sum(rolls_vect)

dice_rolls <- function(n_rolls, dice = 1:6){
  rolls_vect <- vector()
  for(roll in 1:n_rolls){
    num <- sample(dice, 1)
    if(num == 6){
      while(num == 6){
        num <- sample(dice, 1)
      }
    }
    rolls_vect[roll] <- num
  }
  rolls_vect
}

dice_rolls(n_rolls) |> sum()


















