"""
* pp3.py
* Jonathan Pirolo  
* jpirolo         
* ECE 2210, Spring 2026
* PP3
*
* Purpose:  Take in a sample set of threat levels from snort, process the set and determine if a security breach is likely
program should be able to process multiple sets and ends when given a exit code
*
* Assumptions: threat level is always non-negative and <=  2^31. false-postives can happen so we set a threshold
false_alarm_count. We can only process a max of 500 samples at a time and a minimum of 3


* Bugs: There may be some formatting errors, but I didnt find anything wrong functionally.

"""

# You CANNOT import other modules
import sys

# Do NOT change the variable below.
redirectIOtoFile = True

"""
MAXSAMPLES and MINTHREASH are global variables.
In this project, both variables should be treated as a constant. 
This means you should NOT try to change them.
"""
MAXSAMPLES = 500
MINTHRESH = 3


def if_int(l):
	"""Returns True if l can be converted to an integer and False otherwise.
	Args:
		l (str): The return value of input()
	"""
	try:
		int(l)
		return True
	except ValueError:
		return False
	


def process_one_sample_set(dict_threat_count, min_threat_level, false_alarm_count):
	""" Processes one sample set and prints the result.
	
	Args:
		dict_threat_count: Each key of dictionary dict_threat_count is a valid threat value, with the associated value 
							being the count of that threat in one sample set.
		min_threat_level: The user-defined min_threat_value.
		false_alarm_count: The user-defined false_alarm_count.
	"""
	
	highest = None
	for threat in dict_threat_count:
		if threat >= min_threat_level and dict_threat_count[threat] >= false_alarm_count:
			if highest is None or threat > highest:
				highest = threat
	if highest is not None:
		occurrences = dict_threat_count[highest]
		print(f"Threat detected with level {highest} and appears {occurrences} times")
	else:
		print("No threat detected")

def process_sample_sets():
	"""First reads in the min_threat_level and false_alarm_count and then
	continuously processes sample sets one-by-one until a negative value other than -1 is read.

	Args: None
	"""
	min_threat_level = -12345	# This value is expected to change according to user's input
	false_alarm_count = -137153163	# This value is expected to change according to user's input
	
	# Each key of dictionary dict_threat_count is a valid threat value, with the associated value 
	# being the count of that threat in one sample set
	dict_threat_count = dict()	 

	# The following while-loop reads in the min_threat_level. 
	while True:
		min_threat_level = input("What is the minimum threat level (or -1 to exit)?\n")
		if if_int(min_threat_level) and int(min_threat_level)>=MINTHRESH:
			min_threat_level = int(min_threat_level)
			print(f"The minimum threat level is {min_threat_level}")

			break
		elif if_int(min_threat_level) and int(min_threat_level) == -1:
			sys.exit()
		else:
			print("The minimum threat level is invalid.")
		continue

	# The following while-loop reads in the false_alarm_count. 
	while True:	
		false_alarm_count = input("What is the false alarm threshold (or -1 to exit)?\n")	# Replace the break with your code.
		if if_int(false_alarm_count) and int(false_alarm_count) == -1:
			sys.exit()
		elif if_int(false_alarm_count) and int(false_alarm_count) >   0:
			false_alarm_count = int(false_alarm_count)
			print(f"A false alarm if the count is < {false_alarm_count}")
			break
		else:
			print("The false alarm threshold is invalid.")
		continue

	# The following while-loop continuously processes sample sets one-by-one until a negative value other than -1 is read.  		
	sample_count = 0 
	while True:	
		l = input("What is the threat?\n")
		if sample_count == MAXSAMPLES:
			process_one_sample_set(dict_threat_count, min_threat_level, false_alarm_count)
			dict_threat_count.clear()
		if not if_int(l):
			print("threat is invalid")
			continue  # Replace pass with your code
		elif int(l) == -1:
			process_one_sample_set(dict_threat_count, min_threat_level, false_alarm_count)
			dict_threat_count.clear()
		elif int(l) < -1:
			print("Goodbye")
			sys.exit()
		else:
			sample_count +=1
			l = int(l)
			if l in dict_threat_count.keys():
				dict_threat_count[l] += 1
			else:
				dict_threat_count[l] = 1

if __name__ == '__main__':
	""" main function
	"""
	process_sample_sets()


