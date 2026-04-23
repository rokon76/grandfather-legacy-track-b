def main():
    thickness = 0.5  # Using a thinner 0.5mm sample for faster results
    test_temps = [25, 100, 300]  # Celsius
    
    print(f"{'Temp (°C)':<10} | {'Time to Saturation':<20}")
    print("-" * 35)
    
    results_time = []
    
    for temp in test_temps:
        D, time_hours = calculate_kinetics(temp, thickness)
        results_time.append(time_hours)
        
        # Format output: Use minutes if less than 1 hour
        if time_hours < 1:
            time_str = f"{time_hours*60:.2f} minutes"
        else:
            time_str = f"{time_hours:.2f} hours"
            
        print(f"{temp:<10} | {time_str:<20}")

    # Visualization of the Temperature Effect
    plt.figure(figsize=(10, 6))
    plt.bar([f"{t}°C" for t in test_temps], results_time, color=['#34495e', '#e67e22', '#c0392b'])
    plt.ylabel('Time to Saturation (Hours)')
    plt.title(f'Effect of Temperature on {thickness}mm Pd Sample Loading')
    plt.yscale('log') # Log scale because the difference is massive
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
