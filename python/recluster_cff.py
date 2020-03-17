import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *

##################################################################################
######### For AK8 PUPPI jets
finalJetsAK8Constituents = cms.EDProducer("PatJetConstituentPtrSelector",
                                            src = cms.InputTag("updatedJetsAK8"),
                                            cut = cms.string("pt > 170.0")
                                            )
genJetsAK8Constituents = cms.EDProducer("GenJetPackedConstituentPtrSelector",
                                            src = cms.InputTag("slimmedGenJetsAK8"),
                                            cut = cms.string("pt > 100.0")
                                            )



##################### Tables for final output and docs ##########################
finalJetsAK8ConstituentsTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("finalJetsAK8Constituents", "constituents"),
    cut = cms.string(""), #we should not filter after pruning
    name= cms.string("PFCandsAK8"),
    doc = cms.string("interesting gen particles from AK8 jets"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table for the AK8 constituents
    variables = cms.PSet(CandVars,
                            puppiWeight = Var("puppiWeight()", float, doc="Puppi weight",precision=10),
                            puppiWeightNoLep = Var("puppiWeightNoLep()", float, doc="Puppi weight removing leptons",precision=10),
    )
)

##################### Tables for final output and docs ##########################
genJetsAK8ParticleTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("genJetsAK8Constituents", "constituents"),
    cut = cms.string(""), #we should not filter after pruning
    name= cms.string("GenPartAK8"),
    doc = cms.string("interesting gen particles from AK8 jets"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table for the AK8 constituents
    variables = cms.PSet(CandVars
    )
)

##################################################################################
######### For AK4 CHS jets
finalJetsAK4Constituents = finalJetsAK8Constituents.clone( src = 'updatedJets', cut = 'pt>10.0' )
finalJetsAK4ConstituentsTable = finalJetsAK8ConstituentsTable.clone(
                                                                src = cms.InputTag("finalJetsAK4Constituents", "constituents"),
                                                                name= cms.string("PFCandsAK4"),
                                                                doc = cms.string("interesting gen particles from AK4 jets"),
                                                                )
genJetsAK4Constituents = genJetsAK8Constituents.clone(
                                            src = cms.InputTag("slimmedGenJets"),
                                            cut = cms.string("pt > 10.0")
                                            )
genJetsAK4ParticleTable = genJetsAK8ParticleTable.clone(
                                                    src = cms.InputTag("genJetsAK4Constituents", "constituents"),
                                                    name= cms.string("GenPartAK4"),
                                                    doc = cms.string("interesting gen particles from AK4 jets"),
                                                    )

jetReclusterSequence = cms.Sequence(finalJetsAK4Constituents+finalJetsAK8Constituents)
jetReclusterMCSequence = cms.Sequence(genJetsAK4Constituents+genJetsAK8Constituents)
jetReclusterTable = cms.Sequence(finalJetsAK4ConstituentsTable+finalJetsAK8ConstituentsTable)
jetReclusterMCTable = cms.Sequence(genJetsAK4ParticleTable+genJetsAK8ParticleTable)

