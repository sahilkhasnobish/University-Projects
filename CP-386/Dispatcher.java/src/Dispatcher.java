/*
 * Sahil Khasnobish 
 * 190990560 
 * October 19th, 2021
 */
 


import java.util.Queue;
import java.util.Scanner;
import java.util.LinkedList;

public class Dispatcher{
	
	static Queue <process> ready = new LinkedList<>();
	
	static process running_process = null;
	
	static Queue <process> resource1 = new LinkedList<>();
	static Queue <process> resource2 = new LinkedList<>();
	static Queue <process> resource3 = new LinkedList<>();
	
	static LinkedList <process> table = new LinkedList<>();
	
	//get user input, create process, send process to scheduler 
	public static void main(String args[]){// gets user input 
		
		//make system process (process 0)
		process system_process = new process(0, 0, null, 0);//creates the process 
		table.add(system_process);
		//make running process 
		process running_process = new process(0, 0, null, 1);//creates the process 
		table.add(running_process);
		
		Scanner input = new Scanner(System.in);
		String event = input.nextLine();
		
		//keeps looping until there is an empty line, prompts user input 
		
		while(!event.isEmpty()) {
			
			String time_string = "";
			String event_string = "";
			String id_string = "";
			int letter = 0;
			int interrupt = 0;
			
			//process line to extract data 
			for(int i=0;i<event.length()-1;i++) {
				if(Character.isLetter(event.charAt(i))) { //checks to see if a letter is reached
					letter = 1;
				}
				
				//extract the time
				if(letter==0 && event.charAt(i)!=' ') {
					time_string+=Character.toString(event.charAt(i));
					
				//extract the event 
				}else {
					if(event.charAt(i)!=' ') {
						event_string+=Character.toString(event.charAt(i));
					}
				}
			}
			
			//get the process id/see if timer interrupt is indicated 
			if(event.charAt(event.length()-1) == 'T') {
				interrupt = 1;
				event_string = "T";
			}else {
				id_string+=event.charAt(event.length()-1);
			}
			
			if(interrupt == 0) {
				//convert strings into values for PCB (for each process)
				
				int time = Integer.parseInt(time_string);
				int id = Integer.parseInt(id_string);
				String state = event_string;
				int order = table.size()-1;

				process p = new process(id, time, state, order);//creates the process 
				
				
				scheduler(p, interrupt,time); //send process off to dispatcher
			}else {
				process p = null;
				int time = Integer.parseInt(time_string);
				scheduler(p,interrupt,time); //send process off to dispatcher
			}
			
			
			event = input.nextLine(); 
		}
		
		//print output
		int length = table.size();
		for(int i=0;i<length;i++) {
			process p = table.get(i);
			int process_id = p.id;
			
			//get the total time running
			int total_time_running = 0;
			for(int n=0;n<table.get(i).time_running_list.size();n++) {
				total_time_running += table.get(i).time_running_list.get(n);
			}
			
			//get the total time ready
			int total_time_ready = 0;
			for(int n=0;n<table.get(i).time_ready_list.size();n++) {
				total_time_ready += table.get(i).time_ready_list.get(n);
			}
			
			//get the total time blocked
			int total_time_blocked = 0;
			for(int n=0;n<p.time_blocked_list.size();n++) {
				total_time_blocked += table.get(i).time_blocked_list.get(n);
			}
			
			//print process information 
			System.out.printf("%d %d %d %d\n", process_id, total_time_running, total_time_ready, total_time_blocked);
			
		}
		
	}
	
	public static class process{ //process control block 
		
		int id; //process id 
		
		int order;
		//store starting time 
		int time_ready_start = 0;
		int time_running_start = 0;
		int time_blocked_start = 0;
		//store ending time
		int time_ready_end = 0;
		int time_running_end = 0;
		int time_blocked_end = 0;
		
		//store all of the times spent in ready queue, cpu and resources. 
		//later all values will be summed to get the total time spent for each 
		LinkedList <Integer> time_ready_list = new LinkedList<>();
		LinkedList <Integer> time_running_list = new LinkedList<>();
		LinkedList <Integer> time_blocked_list = new LinkedList<>();
		
		int time_running; //total time running 
		int time_ready; //total time ready 
		int time_blocked; //total time blocked 
		int arrival;
		String state; //event 
		
		public process(int process_id, int arrival_time, String process_state, int p_order) {
			this.order = p_order;
			this.id = process_id;
			this.arrival = arrival_time;
			this.time_running = arrival_time;
			this.time_blocked = 0;
			this.time_ready = 0;
			this.state = process_state;
			
			
			//store starting time 
			this.time_ready_start = arrival_time;
			this.time_running_start = arrival_time;
			this.time_blocked_start = arrival_time;
			//store ending time
			this.time_ready_end = time_ready_end;
			this.time_running_end = time_running_end;
			this.time_blocked_end = time_blocked_end;
			
			//store all of the times spent in ready queue, cpu and resources. 
			//later all values will be summed to get the total time spent for each 
			this.time_ready_list = time_ready_list;
			this.time_running_list = time_running_list;
			this.time_blocked_list = time_blocked_list;
			
		}
	}
	
	
	public static void scheduler(process p, int  timer_interrupt, int time){
		
		
		//if a timer interrupt occurs, process in ready queue and running process are swapped 
		
		if(timer_interrupt == 1) { 
			if(!ready.isEmpty()) {
				
				//removes a process from ready queue to send to cpu 
				
				process temp = ready.remove(); //remove value from ready queue
				temp.time_ready_end = time; //get the time for when process leaves ready queue
				temp.time_ready_list.add(temp.time_ready_end-temp.time_ready_start); //save read queue time in list 
				temp.time_running_start = time;
				
				//removes process from cpu and inserts into ready queue 
				
				running_process.time_running_end = time;
				running_process.time_running_list.add(running_process.time_ready_end-running_process.time_ready_start);
				ready.add(running_process); //put running process into ready queue 
				running_process.time_ready_start = time;
				
				
				temp.time_running_start = time;
				running_process = temp; //update the running process
			}
		}else {
			if(p.state.compareTo("C")==0) {
				table.add(p);
				if(ready.isEmpty()) {//process goes straight to cpu if ready queue is empty 
					table.get(p.order).time_running_start = time;	//update cpu time here
					running_process = p; //store process in running process
					
				}else { //process is put inside ready queue to wait for execution 
					ready.add(p);
					table.get(p.order).time_ready_start = time;
				}
			//process is finished, exits 
				
			}else if(p.state.compareTo("E")==0) {
				table.get(p.order).time_running_end = time;
				table.get(p.order).time_running_list.add(table.get(p.order).time_running_end-table.get(p.order).time_running_start); 

			//process is blocked, removed from ready queue and entered into resource block 
			}else if(p.state.compareTo("R1")==0) {
				resource1.add(p);
				table.get(p.order).time_blocked_start = time;
				table.get(p.order).time_ready_end = time;
				table.get(p.order).time_ready_list.add(table.get(p.order).time_ready_end-table.get(p.order).time_ready_start); 
				ready.remove(table.get(p.order));
			}else if(p.state.compareTo("R2")==0) {
				resource2.add(p);
				table.get(p.order).time_blocked_start = time;
				table.get(p.order).time_ready_end = time;
				table.get(p.order).time_ready_list.add(table.get(p.order).time_ready_end-table.get(p.order).time_ready_start); 
				ready.remove(table.get(p.order));
			}else if(p.state.compareTo("R3")==0) {
				resource3.add(p);
				table.get(p.order).time_blocked_start = time;
				table.get(p.order).time_ready_end = time;
				table.get(p.order).time_ready_list.add(table.get(p.order).time_ready_end-table.get(p.order).time_ready_start); 
				ready.remove(table.get(p.order));
				
			//interrupts, processes are removed from resource blocks and entered back into ready queue
				
			}else if(p.state.compareTo("I1")==0) {
				table.get(p.order).time_blocked_end = time;
				table.get(p.order).time_blocked_list.add(table.get(p.order).time_blocked_end-table.get(p.order).time_blocked_start);
				resource1.remove(table.get(p.order));
				ready.add(p);
				p.time_ready_start = time;
			}else if(p.state.compareTo("I2")==0) {
				table.get(p.order).time_blocked_end = time;
				table.get(p.order).time_blocked_list.add(table.get(p.order).time_blocked_end-table.get(p.order).time_blocked_start);
				resource2.remove(table.get(p.order));
				ready.add(table.get(p.order));
				p.time_ready_start = time;
			}else if(p.state.compareTo("I3")==0) {
				table.get(p.order).time_blocked_end = time;
				table.get(p.order).time_blocked_list.add(table.get(p.order).time_blocked_end-table.get(p.order).time_blocked_start);
				resource3.remove(table.get(p.order));
				ready.add(table.get(p.order));
				table.get(p.order).time_ready_start = time;
			}
		}
	}
	
}