from .models import QueryList

def add_query(query,sect,listedd,nbool):
	query_up = QueryList.objects.create(title=query,section=sect,res_list=listedd,qury_bool=nbool)
	query_up.save()