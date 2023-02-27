from televisores.tv import TV

class Control:
    
    def __init__(self, tv):
        self._tv= tv
        
    def turnOn(self,tv):
        self._tv =tv.turnOn()
    
    def turnDown(self,tv):
        self._tv =tv.turnDown()
        
    def canalUp(self,tv):
        self._tv =tv.canalUp()
        
    def canalDown(self,tv):
        self._tv =tv.canalDown()
    
    def volumenUp(self,tv):
        self._tv =tv.volumenUp()
    
    def volumenDown(self,tv):
        self._tv =tv.volumenDown()   
        
    def setCanal(self,tv,canal):
        self._tv = tv.setCanal(canal)
    
    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)
        
    def getTv(self):
        return self._tv
    
    def setTv(self,tv):
        self._tv = tv
        