while True:
	try:
		number = int(input('what is ur fav nmb hoss\n'))
		print(18/number)
		break
	except valueErrow:
		print("make sure and enter a number")
    except zerodivisionerrow:
    	print("dont pick zero")
    except:
    	break
    finally:
    	print("loop complete")
    	