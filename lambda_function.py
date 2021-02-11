import boto3

def lambda_handler(event, context):

	Inf_Instancia	= event["Instancia"];
	Inf_Regiao  	= event["Regiao"];
	Inf_Acao    	= event["Acao"];
	
	if Inf_Acao == "Desligar":
	    
		ec2 = boto3.client('ec2', region_name=Inf_Regiao)
		ec2.stop_instances(InstanceIds=[Inf_Instancia])
		
		return "Desligado"

	else:
	
		ec2 = boto3.client('ec2', region_name=Inf_Regiao)
		ec2.start_instances(InstanceIds=[Inf_Instancia])
		
		return "Ligado"