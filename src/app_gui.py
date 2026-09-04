import os, sys, tkinter as tk
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from neural_network import MLP

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELO = os.path.join(BASE, 'models', 'modelo_entrenado.npz')
NORM = os.path.join(BASE, 'models', 'normalizador.npz')
BG='#08111F'; CARD='#101C2E'; CARD2='#13243A'; TEXT='#F4F7FB'; MUTED='#8EA0B8'; ACCENT='#35D6C7'; GOOD='#36D399'; BAD='#FF667D'

class AppPrediccion(tk.Tk):
    def __init__(self):
        super().__init__(); self.title('PrediScore - Prediccion de Aprobacion'); self.geometry('1000x680'); self.configure(bg=BG)
        self.modelo=MLP.cargar(MODELO); n=np.load(NORM); self.media=n['media']; self.std=n['std']; self._ui()
    def _ui(self):
        tk.Label(self,text='PREDISCORE',bg=BG,fg=ACCENT,font=('Segoe UI',11,'bold')).pack(anchor='w',padx=38,pady=(28,0))
        tk.Label(self,text='Que tan preparado estas?',bg=BG,fg=TEXT,font=('Segoe UI',27,'bold')).pack(anchor='w',padx=38)
        tk.Label(self,text='Ingresa tus datos y descubre una estimacion de tu probabilidad de aprobar.',bg=BG,fg=MUTED,font=('Segoe UI',10)).pack(anchor='w',padx=38,pady=(2,18))
        body=tk.Frame(self,bg=BG); body.pack(fill='both',expand=True,padx=38)
        left=tk.Frame(body,bg=CARD,highlightthickness=1,highlightbackground='#20324A'); left.pack(side='left',fill='both',expand=True,padx=(0,9))
        right=tk.Frame(body,bg=CARD,highlightthickness=1,highlightbackground='#20324A'); right.pack(side='right',fill='both',expand=True,padx=(9,0))
        tk.Label(left,text='Tu informacion',bg=CARD,fg=TEXT,font=('Segoe UI',16,'bold')).pack(anchor='w',padx=24,pady=(22,2))
        tk.Label(left,text='Mueve los controles para ajustar tus valores.',bg=CARD,fg=MUTED,font=('Segoe UI',9)).pack(anchor='w',padx=24,pady=(0,15))
        self.vars=[]
        self._slider(left,'Horas de estudio semanales',0,10,5,0.1,'h')
        self._slider(left,'Asistencia a clases',0,100,80,1,'%')
        self._slider(left,'Nota anterior',0,20,12,0.1,'/ 20')
        tk.Button(left,text='Ver mi probabilidad',command=self.predecir,bg=ACCENT,fg='#061A1A',relief='flat',font=('Segoe UI',11,'bold'),pady=11).pack(fill='x',padx=24,pady=22)
        tk.Label(right,text='Tu resultado',bg=CARD,fg=TEXT,font=('Segoe UI',16,'bold')).pack(anchor='w',padx=24,pady=(22,2))
        tk.Label(right,text='La prediccion es una estimacion del modelo.',bg=CARD,fg=MUTED,font=('Segoe UI',9)).pack(anchor='w',padx=24)
        self.result=tk.Label(right,text='--',bg=CARD,fg=ACCENT,font=('Segoe UI',46,'bold')); self.result.pack(pady=(50,5))
        self.estado=tk.Label(right,text='Aun no hay prediccion',bg=CARD,fg=TEXT,font=('Segoe UI',15,'bold')); self.estado.pack()
        self.msg=tk.Label(right,text='Completa tus datos y pulsa el boton.',bg=CARD,fg=MUTED,font=('Segoe UI',10),wraplength=360,justify='center'); self.msg.pack(padx=30,pady=15)
        self.tip=tk.Label(right,text='Consejo: estudiar con constancia y mantener una buena asistencia puede mejorar tu preparacion.',bg=CARD2,fg='#B8C7DA',font=('Segoe UI',9),wraplength=360,justify='left',padx=16,pady=14); self.tip.pack(fill='x',padx=24,pady=25)
        tk.Label(self,text='Proyecto Final | Sistemas Embebidos y Redes Neuronales | Aracely Estefania Herrera Regalado - Melany Sangoquiza',bg=BG,fg='#62738B',font=('Segoe UI',8)).pack(pady=12)
    def _slider(self,parent,titulo,a,b,valor,paso,unidad):
        box=tk.Frame(parent,bg=CARD); box.pack(fill='x',padx=24,pady=7); top=tk.Frame(box,bg=CARD); top.pack(fill='x')
        tk.Label(top,text=titulo,bg=CARD,fg=TEXT,font=('Segoe UI',10,'bold')).pack(side='left'); v=tk.DoubleVar(value=valor); self.vars.append(v); out=tk.Label(top,text=f'{valor:g} {unidad}',bg=CARD,fg=ACCENT,font=('Segoe UI',10,'bold')); out.pack(side='right')
        def change(x): out.config(text=(f'{float(x):.1f} {unidad}' if paso<1 else f'{float(x):.0f} {unidad}'))
        tk.Scale(box,from_=a,to=b,resolution=paso,orient='horizontal',variable=v,command=change,showvalue=0,bg=CARD,fg=MUTED,troughcolor='#223550',activebackground=ACCENT,highlightthickness=0).pack(fill='x')
    def predecir(self):
        x=np.array([[v.get() for v in self.vars]],float); x=(x-self.media)/(self.std+1e-8); p=float(self.modelo.predict_proba(x)[0,0]); pct=p*100; self.result.config(text=f'{pct:.1f}%')
        if pct>=70: self.estado.config(text='Alta probabilidad de aprobar',fg=GOOD); self.msg.config(text='Tu perfil muestra una buena preparacion. Mantén tus habitos y sigue repasando.')
        elif pct>=50: self.estado.config(text='Probabilidad intermedia',fg=ACCENT); self.msg.config(text='Vas por buen camino. Reforzar tus habitos de estudio puede ayudarte.')
        else: self.estado.config(text='Conviene reforzar tu preparacion',fg=BAD); self.msg.config(text='Dedica mas tiempo al estudio, mejora la asistencia y repasa tus temas clave.')
if __name__=='__main__': AppPrediccion().mainloop()
