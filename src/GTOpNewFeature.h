//Leticia Montalvillo for GitLine



#import <Cocoa/Cocoa.h>
#import	<GDKit/GDKit.h>
#import "GTOpBaseBranchTask.h"

@interface GTOpNewFeature : GTOpBaseBranchTask {
	NSString * startBranchName;
}

- (id) initWithGD:(GittyDocument *)_gd andBranchName:(NSString *) _branchName andStartBranchName:(NSString *) _startBranchName;
- (void) setChecksOutBranch:(BOOL) checksOut;

@end