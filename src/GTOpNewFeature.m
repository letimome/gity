//Leticia Montalvillo for GitLine 2014

#import "GTOpNewFeature.h"

@implementation GTOpNewFeature

- (id) initWithGD:(GittyDocument *)_gd andBranchName:(NSString *) _branchName andStartBranchName:(NSString *) _startBranchName {
	startBranchName = [_startBranchName copy];
	self=[super initWithGD:_gd andBranchName:_branchName];
	return self;
}

- (void) setArguments {
	if([self isCancelled]) return;      //call to python scrip
	[self setArgumentsWithPythonScript:[GTPythonScripts performNewFeature] setArgsOnTask:true];
	[args addObject:[@"-m " stringByAppendingString:branchName]];
	[args addObject:[@"-m " stringByAppendingString:startBranchName]];
	[self updateArguments];
}

- (void) setChecksOutBranch:(BOOL) checksOut {
	if(checksOut) {
		[args addObject:[@"-m " stringByAppendingString:@"1"]];
	}
	[self updateArguments];
}

- (void) dealloc {
#ifdef GT_PRINT_DEALLOCS
	printf("DEALLOC GTOpNewFeature\n");
#endif
	GDRelease(startBranchName);
}

@end