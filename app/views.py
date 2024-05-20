from django.shortcuts import render 


# defining function for wordcounter 
def counter(request): 
	# checking if method is POST or not 
	if request.method == 'POST': 

		# taking text input 
		text = request.POST['texttocount'] 

		# checking weather text is empty 
		# or not 
		if text != '': 

			# splitting the text and taking length 
			# of that 
			word = len(text.split()) 

			# defining boolean so that we can keep 
			# track of process later 
			i = True

			# returning HTML page with data, if calculated 
			# successfully 
			return render(request, 'counter.html', 
						{'word': word, 'text': text, 'i': i, 'on': 'active'}) 

		else: 
			# returning HTML page without data, if any 
			# error occurs 
			return render(request, 'counter.html', {'on': 'active'}) 

	else: 
		# returning HTML page if request.method is not POST 
		return render(request, 'counter.html', {'on': 'active'})
