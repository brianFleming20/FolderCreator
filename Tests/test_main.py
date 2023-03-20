import pathlib
import main
import os

path = os.path.join("C:\\Users\\BrianFleming\\Desktop", "")


class Test_main():

    def test_currentuser(self):
        user = main.current_user
        current_user = os.path.join(os.environ['USERPROFILE'])
        assert user == current_user

    def test_search_for_path(self):
        check_endpoint = "Daily probe log"
        path = main.search_data_path()
        endpath = pathlib.PurePath(path).name
        assert endpath == check_endpoint

    def test_create_base_folder(self):
        batch = "12345"
        b_type = "DP240"
        file = f"{batch} {b_type}"
        test_path = os.path.join(path, file)
        main.create_base_folder(test_path)
        if os.path.exists(test_path):
            assert True
        else:
            assert False

    def test_create_folders(self):
        batch = "12345 I2C"
        t_path = os.path.join(path, batch)
        letters = ["A", "B", "C"]
        main.batch.set("12345")
        main.search_item.set("I2C")
        index = 0
        main.create_data_folders(letters, t_path)
        for letter in os.listdir(t_path):
            if letters[index] in letter:
                assert True
            index += 1

    def test_generate_folders(self):
        main.batch.set("12345")
        main.search_item.set("DP240")
        main.data_path.set(path)
        test_path = os.path.join(path, "12345 DP240")
        index = 0
        letters = ["A", "B", "C", "D"]
        main.generate_folders("A", "D")
        if os.path.exists(test_path):
            assert True
        else:
            assert False
        ####################################
        # Add to an existing file without  #
        # altering any files present       #
        ####################################
        for letter in os.listdir(test_path):
            if letters[index] in letter:
                assert True
            index += 1

        index = 0
        new_letters = ["A", "B", "C", "D", "E", "F", "G"]
        main.generate_folders("A", "G")
        for letter in os.listdir(test_path):
            if new_letters[index] in letter:
                assert True
            index += 1

    def test_generate(self):
        ###################################
        # Test if the use has not filled  #
        # in the display.                 #
        ###################################
        main.batch.set("")
        main.search_item.set("DP12")
        main.data_path.set(path)
        main.test = True
        result = main.generate()
        assert not result
        ###################################
        # The user has used a complete    #
        # batch number instead of the     #
        # base as requested.              #
        ###################################
        main.batch.set("12345a")
        main.first_letter.set("a")
        main.last_letter.set("d")
        result1 = main.generate()
        assert not result1
        ###################################
        # The user fills in the display   #
        # correctly.                      #
        ###################################
        main.batch.set("12345")
        main.first_letter.set("a")
        main.last_letter.set("d")
        result2 = main.generate()
        assert result2
        ###################################
        # The user fills in the display   #
        # correctly and there are folders #
        # already created.                #
        ###################################
        main.batch.set("12345")
        main.first_letter.set("a")
        main.last_letter.set("g")
        result2 = main.generate()
        assert not result2

    def test_search_format(self):
        format1 = "12345A DP240"
        format2 = "12345 A DP240"
        format3 = "12345A-DP240"
        format4 = "12345-A /DP12"
        batch = "12345"
        new_batch = "23476B DP12"

        result = main.search_format(format4, batch)
        result1 = main.create_new_format(result, new_batch, batch)
        print(result1)

    def test_new_format(self):
        new_format_data = ['45', 'L', '32', '47', 'L', 'L', 'N', 'N', 'N']
        new_batch = "23476B DP240"
        batch = "23476"

        result = main.create_new_format(new_format_data, new_batch, batch)
        print(result)



