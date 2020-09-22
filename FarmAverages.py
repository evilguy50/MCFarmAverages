from keyboard import read_key


def farm_averages(drops, hours):
    average = drops / hours
    print("Your farm averages about " + str(round(average)) + " drops per hour.")


farm_averages(drops=eval(input("How many drops did you get from your afk session?: \n")),
             hours=eval(input("How many hours were you afk?\n")))


print("Press any key to exit program")
read_key()