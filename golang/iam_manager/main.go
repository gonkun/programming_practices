package main

import (
	"context"
	"log"

	"github.com/aws/aws-sdk-go-v2/config"
)

func main() {
	// Load the Shared AWS Configuration (~/.aws/config)
	cfg, err := config.LoadDefaultConfig(context.TODO(),
		config.WithRegion("eu-west-1"),
		config.WithSharedConfigProfile("userzoom-dev"))
	if err != nil {
		log.Fatal(err)
	}

	// Create an Amazon IAM service client
	client := iam.NewFromConfig(cfg)

}
