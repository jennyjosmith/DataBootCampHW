## import the standard stuff
import csv
import os

# These are my files
file_data = os.path.join("/Users/Admin/Desktop/election_data2.csv")
file_final = os.path.join("/Users/Admin/Desktop/election_results.csv")

with open(file_data) as election_data:
    reader = csv.reader(election_data)

  # Read header row. Because we've already read the header row, the for loop
    # below will begin at the second line where the actual data begins.
    header_row = next(reader)

 # identify column indices 
   
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        ## ^^ result is 0 for voter id, 1 for county and 2 for candidate


# What I need to calculate

# counter: 
total_votes = 0
# ^^ counter. each vote is a row, so initally set coutner to 0

# lists:
candidate_list = []
# ^ [] designates a list capture (that can be altered)
votes_per_candidate = {}
# ^^ {} designates an associative array (dictionary)

# results:
winner = ""
winner_votes = 0

# read csv and convert into dictionaries (associative array)
# see if this will work without the below open/header reader being in here 
# a second time
with open(file_data) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_list:

            # Add it to the list of candidates in the running
            candidate_list.append(candidate_name)

            # And begin tracking that candidate's voter count
            votes_per_candidate[candidate_name] = 0

        # Then add a vote to that candidate's count
        votes_per_candidate[candidate_name] = votes_per_candidate[candidate_name] + 1

# Print the results and export the data to our text file
with open(file_final, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in votes_per_candidate:

        # Retrieve vote count and percentage
        votes = votes_per_candidate.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winner_votes):
            winner_votes = votes
            winner = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winner_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winner_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winner_summary)

