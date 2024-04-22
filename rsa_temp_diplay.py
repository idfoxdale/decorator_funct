from flask import Flask, render_template, request
import paramiko

app = Flask(__name__)

def generate_ssh_key_pair(username, password, key_filename):
    # Generate an RSA key pair with a passphrase
    rsa_key = paramiko.RSAKey.generate(2048)

    # Save the private key to a file with the given filename
    rsa_key.write_private_key_file(key_filename, password=password)

    # Save the public key to a file with the given filename + ".pub"
    with open(key_filename + ".pub", "w") as pub_key_file:
        pub_key_file.write(f"{rsa_key.get_name()} {rsa_key.get_base64()}")

    print(f"SSH key pair generated successfully: {key_filename} and {key_filename}.pub")

def ssh_connection_demo(username, private_key_path, hostname, port=22):
    # Create a new SSH client
    ssh_client = paramiko.SSHClient()

    # Automatically add the host key to the local store
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Load the private key
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path, password="demo_password")

        # Connect to the SSH server using the private key for authentication
        ssh_client.connect(hostname, port, username, pkey=private_key)

        print("SSH connection established successfully!")

        # Return the connection status
        return "SSH connection established successfully!"

    except paramiko.AuthenticationException:
        return "Authentication failed. Please check your credentials."
    except paramiko.SSHException as e:
        return f"SSH connection failed: {e}"
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        # Close the SSH connection
        ssh_client.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        hostname = request.form['hostname']
        key_filename = request.form['key_filename']

        # Generate SSH key pair (for demo purposes only)
        generate_ssh_key_pair(username, "demo_password", key_filename)

        # Establish SSH connection using the generated keys
        private_key_path = key_filename
        connection_status = ssh_connection_demo(username, private_key_path, hostname)
        
        return render_template('index.html', connection_status=connection_status)
    
    # Render the initial form
    return render_template('index.html', connection_status=None)

if __name__ == "__main__":
    app.run(debug=True)
