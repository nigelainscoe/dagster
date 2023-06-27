// Generated GraphQL types, do not edit manually.

import * as Types from '../../../graphql/types';

export type GetEvaluationsQueryVariables = Types.Exact<{
  assetKey: Types.AssetKeyInput;
  limit: Types.Scalars['Int'];
  cursor?: Types.InputMaybe<Types.Scalars['String']>;
}>;

export type GetEvaluationsQuery = {
  __typename: 'Query';
  autoMaterializeAssetEvaluationsOrError:
    | {__typename: 'AutoMaterializeAssetEvaluationNeedsMigrationError'; message: string}
    | {
        __typename: 'AutoMaterializeAssetEvaluationRecords';
        currentEvaluationId: number | null;
        records: Array<{
          __typename: 'AutoMaterializeAssetEvaluationRecord';
          id: string;
          evaluationId: number;
          numRequested: number;
          numSkipped: number;
          numDiscarded: number;
          timestamp: number;
          conditions: Array<
            | {
                __typename: 'DownstreamFreshnessAutoMaterializeCondition';
                decisionType: Types.AutoMaterializeDecisionType;
              }
            | {
                __typename: 'FreshnessAutoMaterializeCondition';
                decisionType: Types.AutoMaterializeDecisionType;
              }
            | {
                __typename: 'MaxMaterializationsExceededAutoMaterializeCondition';
                decisionType: Types.AutoMaterializeDecisionType;
              }
            | {
                __typename: 'MissingAutoMaterializeCondition';
                decisionType: Types.AutoMaterializeDecisionType;
              }
            | {
                __typename: 'ParentMaterializedAutoMaterializeCondition';
                decisionType: Types.AutoMaterializeDecisionType;
              }
            | {
                __typename: 'ParentOutdatedAutoMaterializeCondition';
                decisionType: Types.AutoMaterializeDecisionType;
              }
          >;
        }>;
      }
    | null;
};

export type GetPolicyInfoQueryVariables = Types.Exact<{
  assetKey: Types.AssetKeyInput;
}>;

export type GetPolicyInfoQuery = {
  __typename: 'Query';
  assetNodeOrError:
    | {
        __typename: 'AssetNode';
        id: string;
        freshnessPolicy: {
          __typename: 'FreshnessPolicy';
          maximumLagMinutes: number;
          cronSchedule: string | null;
          cronScheduleTimezone: string | null;
        } | null;
        autoMaterializePolicy: {
          __typename: 'AutoMaterializePolicy';
          policyType: Types.AutoMaterializePolicyType;
          maxMaterializationsPerMinute: number | null;
        } | null;
      }
    | {__typename: 'AssetNotFoundError'};
};
