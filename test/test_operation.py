

from src import add, sub, multiply  



def test_add():
    assert add(2,3)==5
    assert add(1,1)==2
    assert add(2,4)==6
    assert add(6,3)==9

def test_sub():
    assert sub(2,1)==1    
    assert sub(2,0)==2   
    assert sub(4,1)==3   
    assert sub(6,1)==5   
    assert sub(17,10)==7   
    assert sub(18,11)==7   
    assert sub(19,12)==7  
def test_mul():
    assert sub(2,4)==8     
    assert sub(4,4)==16     
    assert sub(2,9)==18     
    assert sub(3,11)!=22    