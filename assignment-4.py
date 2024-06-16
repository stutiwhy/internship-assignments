feedbacks = ['feedback1.txt', 'feedback2.txt', 'feedback3.txt'] # list containing names of all files to be read

def read_files(): # function to read all files in feedbacks list
    fb = [] # empty list to store data from files
    for name in feedbacks:
        try:
            with open(name, 'r') as f:
                lines = f.readlines()
                fb.extend([line.strip() for line in lines]) # strip() to get rid of \n everywhere
        except FileNotFoundError as f: # error handling
            print(f"File {name} not found. {f}")

    return fb

def split_file_data(fb): # function to split fb into meaningful variables
    fb_data = [] # empty list to store dicts of data later
    rating_sum = 0
    for feedback in fb:
        try:
            splitted = feedback.split(': ',1)
            name = splitted[0]
            rest = splitted[1]
            splitted = rest.split(' - ')
            rating = splitted[0]
            comment = splitted[1]
            rating = int(rating) # typecasting rating from string to int to calculate avg later
            fb_data.append({'name' : name, 'rating' : rating, 'comment' : comment}) # appending dicts of each feedback into list
            rating_sum += rating # for avg calculation
        except ValueError as v: # error handling
            print(f"A value error occured in : {feedback}. {v}")

    return rating_sum, fb_data

def find_avg_rating(rating_sum, fb_data): # function to calculate average rating
    if len(fb_data) > 0:
        avg_rating = rating_sum / len(fb_data)
    else: # if no data in file, avg rating set to zero
        avg_rating = 0.0
         
    return avg_rating

def write_summary_file(avg_rating, fb_data): # function to write all processed data into summary file
    try:
        with open("feedback_summary.txt", 'w') as f: # opening summary file
            total = len(fb_data) # total entries
            f.write(f"Total Feedback Entries: {total}")
            f.write(f"\nAverage Rating: {avg_rating:.2f}") # displaying only 2 digits after decimal point
            f.write("\n\nFeedbacks:")
            for feedback in fb_data:
                f.write(f"\n{feedback['name']}: {feedback['rating']} - {feedback['comment']}") # accessing elements of dicts of list by their keys
        print("Summary file made successfully !")
    except IOError as i: # error handling
        print(f"There has been an error writing to the file 'feedback_summary.txt'. {i}")

def main(): # using the functions made above
    fb = read_files()
    rating_sum, fb_data = split_file_data(fb)
    avg_rating = find_avg_rating(rating_sum, fb_data)
    write_summary_file(avg_rating, fb_data)

main()