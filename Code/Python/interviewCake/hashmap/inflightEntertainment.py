def flight_movie(flight_length,movie_length):
    happy = False
    movie_time = set(movie_length)
    
    for i in movie_time:
        n = flight_length - i
        if n in movie_length:
            happy = True
            return happy
        
    return happy

def flight_movie2(flight_length,movie_length):
    movie_time = set()
    
    for i in movie_length:
        n = flight_length - i
        if n in movie_time:
            return True
        
        movie_time.add(i)
    return False
    

def main():
    times = flight_movie2(12, [2,3,4,5,7,8,5,3])
    times2 = flight_movie2(12, [12,1,1,71,1,1,1])
    print(times, times2, sep="\n")
if __name__ == "__main__":
    main()