from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli

def run_command(task):
    command_to_run = ['show ip int br','show version']

    result = task.run(task=napalm_cli, commands=command_to_run)

    return result[0].result

if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")

    print("\n--- Running CLI Command on Devices ---")
    results = nr.run(task=run_command)

    for host_name, multi_result in results.items():
        print("="*20)
        print(f"Showing Results for: {host_name}")
        print("="*20)

        if multi_result.failed:
            print(f"Task failed for {host_name}. Error. {multi_result[0].exception}")

        else:
            command_output = multi_result[0].result

            for command, output in command_output.items():
                print(f"\n--- Output for command: {command} ---")
                print(output)