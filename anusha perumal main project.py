import tkinter as tk
from tkinter import messagebox,filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
class SalesForecastingSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Machine Learning Based Sales Forecasting System")
        self.root.geometry("1000x650")
        self.data=None
        self.models={}
        self.results=[]
        self.best_model=None
        self.best_model_name=None
        self.features=["Quantity","Price","Discount","Day","Month","Year","DayOfWeek","Week","Sales_Lag1","Sales_Lag7","MovingAverage7"]
        self.create_interface()
    def create_interface(self):
        tk.Label(self.root,text="Machine Learning Based Sales Forecasting System",font=("Arial",20,"bold")).pack(pady=15)
        frame=tk.Frame(self.root)
        frame.pack(pady=10)
        tk.Label(frame,text="Select Option:",font=("Arial",12,"bold")).pack(side="left",padx=5)
        self.choice=tk.StringVar()
        self.choice.set("Select Option")
        options=["Load Sales Data","Train ML Models","Forecast Sales","Sales Analysis","Model Comparison","What-If Analysis"]
        tk.OptionMenu(frame,self.choice,*options).pack(side="left",padx=5)
        tk.Button(frame,text="Run",width=12,height=2,command=self.run_option).pack(side="left",padx=5)
        self.result=tk.Text(self.root,width=115,height=28,font=("Consolas",10))
        self.result.pack(padx=15,pady=15)
    def run_option(self):
        option=self.choice.get()
        if option=="Load Sales Data":
            self.load_data()
        elif option=="Train ML Models":
            self.train_models()
        elif option=="Forecast Sales":
            self.forecast_sales()
        elif option=="Sales Analysis":
            self.sales_analysis()
        elif option=="Model Comparison":
            self.model_comparison()
        elif option=="What-If Analysis":
            self.what_if_analysis()
        else:
            messagebox.showwarning("Warning","Please select an option")
    def load_data(self):
        file=filedialog.askopenfilename(title="Select Sales CSV File",filetypes=[("CSV Files","*.csv")])
        if not file:
            return
        try:
            self.data=pd.read_csv(file)
            required=["Date","Sales","Quantity","Price","Discount"]
            missing=[x for x in required if x not in self.data.columns]
            if missing:
                messagebox.showerror("Invalid CSV","Missing columns: "+str(missing))
                self.data=None
                return
            self.data["Date"]=pd.to_datetime(self.data["Date"],errors="coerce")
            for col in ["Sales","Quantity","Price","Discount"]:
                self.data[col]=pd.to_numeric(self.data[col],errors="coerce")
            self.data=self.data.dropna(subset=required)
            self.result.delete("1.0",tk.END)
            self.result.insert(tk.END,"SALES DATA LOADED SUCCESSFULLY\n")
            self.result.insert(tk.END,"Total Records: "+str(len(self.data))+"\n")
            self.result.insert(tk.END,str(self.data.head(10)))
            messagebox.showinfo("Success","Sales data loaded successfully")
        except Exception as e:
            messagebox.showerror("Load Error",str(e))
    def prepare_data(self):
        df=self.data.copy()
        df=df.drop_duplicates()
        df=df.sort_values("Date")
        df["Day"]=df["Date"].dt.day
        df["Month"]=df["Date"].dt.month
        df["Year"]=df["Date"].dt.year
        df["DayOfWeek"]=df["Date"].dt.dayofweek
        df["Week"]=df["Date"].dt.isocalendar().week.astype(int)
        df["Sales_Lag1"]=df["Sales"].shift(1)
        df["Sales_Lag7"]=df["Sales"].shift(7)
        df["MovingAverage7"]=df["Sales"].shift(1).rolling(7).mean()
        df=df.dropna()
        return df
    def train_models(self):
        if self.data is None:
            messagebox.showwarning("Warning","Please load sales data first")
            return
        try:
            df=self.prepare_data()
            if len(df)<20:
                messagebox.showwarning("Warning","At least 20 records are required")
                return
            X=df[self.features]
            y=df["Sales"]
            split=int(len(df)*0.8)
            X_train=X.iloc[:split]
            X_test=X.iloc[split:]
            y_train=y.iloc[:split]
            y_test=y.iloc[split:]
            self.models={"Linear Regression":LinearRegression(),"Random Forest":RandomForestRegressor(n_estimators=100,random_state=42),"Gradient Boosting":GradientBoostingRegressor(n_estimators=100,random_state=42)}
            self.results=[]
            for name,model in self.models.items():
                model.fit(X_train,y_train)
                prediction=model.predict(X_test)
                mae=mean_absolute_error(y_test,prediction)
                rmse=np.sqrt(mean_squared_error(y_test,prediction))
                r2=r2_score(y_test,prediction)
                self.results.append({"Model":name,"MAE":mae,"RMSE":rmse,"R2":r2})
            self.results.sort(key=lambda x:x["R2"],reverse=True)
            self.best_model_name=self.results[0]["Model"]
            self.best_model=self.models[self.best_model_name]
            self.result.delete("1.0",tk.END)
            self.result.insert(tk.END,"MODEL PERFORMANCE\n")
            for item in self.results:
                self.result.insert(tk.END,"Model: "+item["Model"]+"\n")
                self.result.insert(tk.END,"MAE: "+f"{item['MAE']:.2f}"+"\n")
                self.result.insert(tk.END,"RMSE: "+f"{item['RMSE']:.2f}"+"\n")
                self.result.insert(tk.END,"R2: "+f"{item['R2']:.4f}"+"\n")
            self.result.insert(tk.END,"BEST MODEL: "+self.best_model_name)
            messagebox.showinfo("Training Complete","Best Model: "+self.best_model_name)
        except Exception as e:
            messagebox.showerror("Training Error",str(e))
    def forecast_sales(self):
        if self.best_model is None:
            messagebox.showwarning("Warning","Please train the ML models first")
            return
        try:
            df=self.prepare_data()
            history=list(df["Sales"])
            last=df.iloc[-1]
            predictions=[]
            for i in range(1,8):
                future=last["Date"]+pd.Timedelta(days=i)
                input_data=pd.DataFrame([{"Quantity":last["Quantity"],"Price":last["Price"],"Discount":last["Discount"],"Day":future.day,"Month":future.month,"Year":future.year,"DayOfWeek":future.dayofweek,"Week":int(future.isocalendar().week),"Sales_Lag1":history[-1],"Sales_Lag7":history[-7],"MovingAverage7":np.mean(history[-7:])}])
                prediction=max(0,float(self.best_model.predict(input_data[self.features])[0]))
                predictions.append((future,prediction))
                history.append(prediction)
            self.result.delete("1.0",tk.END)
            self.result.insert(tk.END,"7 DAY SALES FORECAST\n")
            self.result.insert(tk.END,"Best Model: "+self.best_model_name+"\n")
            for date,value in predictions:
                self.result.insert(tk.END,date.strftime("%d-%m-%Y")+" -> "+f"{value:.2f}"+"\n")
            plt.figure(figsize=(9,5))
            plt.plot([x[0] for x in predictions],[x[1] for x in predictions],marker="o")
            plt.title("7 Day Sales Forecast")
            plt.xlabel("Date")
            plt.ylabel("Predicted Sales")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            messagebox.showerror("Forecast Error",str(e))
    def sales_analysis(self):
        if self.data is None:
            messagebox.showwarning("Warning","Please load sales data first")
            return
        try:
            total=self.data["Sales"].sum()
            average=self.data["Sales"].mean()
            maximum=self.data["Sales"].max()
            minimum=self.data["Sales"].min()
            highest=self.data.loc[self.data["Sales"].idxmax()]
            lowest=self.data.loc[self.data["Sales"].idxmin()]
            self.result.delete("1.0",tk.END)
            self.result.insert(tk.END,"SALES ANALYSIS\n")
            self.result.insert(tk.END,"Total Sales: "+f"{total:.2f}"+"\n")
            self.result.insert(tk.END,"Average Sales: "+f"{average:.2f}"+"\n")
            self.result.insert(tk.END,"Maximum Sales: "+f"{maximum:.2f}"+"\n")
            self.result.insert(tk.END,"Minimum Sales: "+f"{minimum:.2f}"+"\n")
            self.result.insert(tk.END,"Highest Sales Date: "+str(highest["Date"])+"\n")
            self.result.insert(tk.END,"Lowest Sales Date: "+str(lowest["Date"]))
        except Exception as e:
            messagebox.showerror("Analysis Error",str(e))
    def model_comparison(self):
        if not self.results:
            messagebox.showwarning("Warning","Please train the models first")
            return
        self.result.delete("1.0",tk.END)
        self.result.insert(tk.END,"MODEL COMPARISON\n")
        for rank,item in enumerate(self.results,start=1):
            self.result.insert(tk.END,"Rank: "+str(rank)+"\n")
            self.result.insert(tk.END,"Model: "+item["Model"]+"\n")
            self.result.insert(tk.END,"MAE: "+f"{item['MAE']:.2f}"+"\n")
            self.result.insert(tk.END,"RMSE: "+f"{item['RMSE']:.2f}"+"\n")
            self.result.insert(tk.END,"R2: "+f"{item['R2']:.4f}"+"\n")
        self.result.insert(tk.END,"BEST MODEL: "+self.best_model_name)
    def what_if_analysis(self):
        if self.best_model is None:
            messagebox.showwarning("Warning","Please train the model first")
            return
        window=tk.Toplevel(self.root)
        window.title("What-If Sales Analysis")
        window.geometry("400x300")
        tk.Label(window,text="Price Change (%)").pack(pady=10)
        price_entry=tk.Entry(window)
        price_entry.pack()
        tk.Label(window,text="Discount Change (%)").pack(pady=10)
        discount_entry=tk.Entry(window)
        discount_entry.pack()
        def calculate():
            try:
                price_change=float(price_entry.get())
                discount_change=float(discount_entry.get())
                row=self.prepare_data().iloc[-1]
                new_price=row["Price"]*(1+price_change/100)
                new_discount=max(0,min(100,row["Discount"]+discount_change))
                input_data=pd.DataFrame([{"Quantity":row["Quantity"],"Price":new_price,"Discount":new_discount,"Day":row["Day"],"Month":row["Month"],"Year":row["Year"],"DayOfWeek":row["DayOfWeek"],"Week":row["Week"],"Sales_Lag1":row["Sales"],"Sales_Lag7":row["Sales_Lag7"],"MovingAverage7":row["MovingAverage7"]}])
                prediction=max(0,float(self.best_model.predict(input_data[self.features])[0]))
                messagebox.showinfo("What-If Result","Predicted Sales: "+f"{prediction:.2f}")
            except ValueError:
                messagebox.showerror("Input Error","Please enter valid numbers")
            except Exception as e:
                messagebox.showerror("Error",str(e))
        tk.Button(window,text="Calculate Prediction",command=calculate).pack(pady=25)
root=tk.Tk()
app=SalesForecastingSystem(root)
root.mainloop()
