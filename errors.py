def error_demo():
    try:
        # NameError
        print(a)

        # TypeError
        result = "string" + 5

        # ValueError
        num = int("abc")

        # IndexError
        my_list = [1, 2, 3]
        print(my_list[10])

        # KeyError
        my_dict = {"name": "Alice"}
        print(my_dict["age"])

        # AttributeError
        x = 10
        x.append(5)

        # ZeroDivisionError
        print(5 / 0)

        # FileNotFoundError
        with open("newfile.txt", "r") as f:
            content = f.read()

        # ImportError / ModuleNotFoundError
        import new_module

    except NameError as e:
        print("NameError caught:", e)

    except TypeError as e:
        print("TypeError caught:", e)

    except ValueError as e:
        print("ValueError caught:", e)

    except IndexError as e:
        print("IndexError caught:", e)

    except KeyError as e:
        print("KeyError caught:", e)

    except AttributeError as e:
        print("AttributeError caught:", e)

    except ZeroDivisionError as e:
        print("ZeroDivisionError caught:", e)

    except FileNotFoundError as e:
        print("FileNotFoundError caught:", e)

    except ImportError as e:
        print("ImportError or ModuleNotFoundError caught:", e)

    else:
        print("No errors occurred.")

    finally:
        print("Execution of try-except block is complete.")


error_demo()
